from rest_framework import serializers

from api.models import File


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ('file',)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name', 'file', 'uploaded_at', 'processed')
