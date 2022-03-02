from django.urls import path

from ahypotenuse import views

app_name='ahypotenuse'

urlpatterns = [
    path('hypotenuse', views.hypotenuse, name='hypotenuse'),
    path('youhypotenuse', views.youhypotenuse, name='youhypotenuse'),
]
