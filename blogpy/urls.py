
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(r'', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static('contact/static/', document_root = settings.STATIC_ROOT)
