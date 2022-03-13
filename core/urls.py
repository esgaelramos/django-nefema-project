from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('ahello.urls', namespace='ahello')),

    path('', include('ahypotenuse.urls', namespace='ahypotenuse')),

    path('', include('agpassword.urls', namespace='agpassword')),

    path('', include('acourses.urls', namespace='acourses')),

    path('', include('amailcontact.urls', namespace='amailcontact')),

    path('api/', include('apihelloview.urls', namespace='apihelloview')),

    path('api/', include('apiblogview.urls', namespace='apiblogview')),

    # path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
