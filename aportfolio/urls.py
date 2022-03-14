from django.urls import path

from aportfolio import views

app_name='aportfolio'

urlpatterns = [
    path('portfolio', views.portfolio, name='portfolio'),
]