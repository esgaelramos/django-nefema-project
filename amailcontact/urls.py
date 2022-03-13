from django.urls import path

from amailcontact import views

app_name='amailcontact'

urlpatterns = [
    path('contact-form/', views.contactForm),
    path('contact/', views.contact),
]