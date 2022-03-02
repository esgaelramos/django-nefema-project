from django.urls import path

from agpassword import views

app_name='agpassword'

urlpatterns = [
    path('password', views.password, name='password'),
    path('youpassword', views.youpassword, name='youpassword'),
]
