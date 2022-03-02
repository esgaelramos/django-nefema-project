from django.urls import path

from ahello import views

app_name='ahello'

urlpatterns = [
    path('', views.home, name='home'),
    path('hello-world', views.HelloWorld, name='hello-world'),
]
