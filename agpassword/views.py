from django.shortcuts import render
import random

# Create your views here.
def password(request):
    return render(request, 'password.html')

def youpassword(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@!?-_#$%&/()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    for x in range(length):
        generated_password += random.choice(characters)


    return render(request, 'youpassword.html', {'password': generated_password})
