from django.urls import path

from apihelloview import views

app_name='apihelloview'

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
]