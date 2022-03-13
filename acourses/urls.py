from django.urls import path

from acourses import views

app_name='acourses'

urlpatterns = [
    path('courses', views.home, name='courses'),
    path('registrarCurso/', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('edicionCurso/', views.edicionCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
]
