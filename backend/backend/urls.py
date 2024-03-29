from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.urls import api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += api_urlpatterns

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
