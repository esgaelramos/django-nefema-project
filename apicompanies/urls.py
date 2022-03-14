from django.urls import path

from .views import CompanyView

app_name='apicompanies'

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process')
]