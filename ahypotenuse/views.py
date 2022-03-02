from django.shortcuts import render

# Create your views here.

def hypotenuse(request):
    return render(request, 'hypotenuse.html')

def youhypotenuse(request):

    def calculateHipotenusa(catetoa, catetob):
        catetoa = catetoa ** 2
        catetob = catetob ** 2
        catetoc = (catetoa + catetob) ** 0.5
        return round(catetoc, 2)
    
    catetoa = int(request.GET.get('catetoa'))
    catetob = int(request.GET.get('catetob'))
    catetoA2 = catetoa**2
    catetoB2 = catetob**2 
    cateto_suma = catetoB2 + catetoA2

    hipotenusa = calculateHipotenusa(catetoa, catetob)
    
    return render(request, 'youhypotenuse.html', {'hipotenusa': hipotenusa, 'catetoa': catetoa, 'catetob': catetob, 'catetoA': catetoA2, 'catetoB': catetoB2, 'catetoS': cateto_suma})
