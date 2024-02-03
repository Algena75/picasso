from rest_framework.routers import DefaultRouter
from .views import FileViewSet, FileUploadViewSet


router = DefaultRouter()

router.register(r'files', FileViewSet, basename='files')
router.register(r'upload', FileUploadViewSet, basename='loads')
api_urlpatterns = router.urls
