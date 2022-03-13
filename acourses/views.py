from django.shortcuts import redirect, render
from .models import Course

# Create your views here.
def home(request):
    cursosListados = Course.objects.all()
    return render(request, 'managerCourses.html', {'cursos': cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCode']
    nombre = request.POST['txtName']
    creditos = request.POST['numCredits']

    curso = Course.objects.create(ac_code=codigo, ac_name=nombre, ac_credits=creditos)
    
    return redirect('/courses')

def editarCurso(request, codigo):
    curso = Course.objects.get(ac_code=codigo)
    return render(request, 'editCourses.html', {'curso': curso})

def edicionCurso(request):
    codigo = request.POST['txtCode']
    nombre = request.POST['txtName']
    creditos = request.POST['numCredits']
    curso = Course.objects.get(ac_code=codigo)

    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()

    return redirect('/courses')


def eliminarCurso(request, codigo):
    curso = Course.objects.get(ac_code=codigo)
    curso.delete()
    
    return redirect('/courses')
