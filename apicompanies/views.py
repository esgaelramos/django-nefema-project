from django.views import View
from .models import Company
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

#Existen VIEWS about CLASS and about FUNCTIONS;

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                data = {
                    'message': 'Success',
                    'companies': company,
                }
            else:
                data = {
                    'message': 'Error: Companies not found...'
                }
            return JsonResponse(data)
        else:
            # companies = Company.objects.all()
            companies = list(Company.objects.values())
            if len(companies) > 0:
                data = {
                    'message': 'Success',
                    'companies': companies,
                }
            else:
                data = {
                    'message': 'Error: Companies not found...'
                }
            return JsonResponse(data)
    
    
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        data = {
            'message': 'Success',
        }
        return JsonResponse(data)
        

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            data = {'message': 'Success'}
        else:
            data = {
                'message': 'Error: Company not Found...'
            }
        return JsonResponse(data)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            data = {
                'message': 'Success',
            }
        else:
            data = {
                'message': 'Error: Company not Found...'
            }
        return JsonResponse(data)
