from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.exceptions import APIException
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

# from api.tasks import handle_file
from api.models import File
from api.serializers import FileSerializer, FileUploadSerializer
from handler.tasks import get_handler


class FileUploadViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializer
    http_method_names = ('post',)

    def create(self, request):
        try:
            with transaction.atomic():
                serializer = FileUploadSerializer(data=request.data)
                if serializer.is_valid():
                    file = File.objects.create(**serializer.validated_data)
                    job_params = {"db_id": file.id, "file_name": file.name}
                    transaction.on_commit(
                        lambda: get_handler.delay(job_params)
                    )
                    return Response(
                        FileSerializer(file).data,
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as error:
            raise APIException(str(error))
        

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    http_method_names = ('get',)
