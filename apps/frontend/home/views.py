from django.shortcuts import render
from django.views import View
from apps.frontend.home.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class Home(View):

    template_location = 'frontend/index.html'

    def get(self, request):
        return render(request, self.template_location)

    def post(self, request):
        pet_name = request.POST['pet-name']
        pet_breed = request.POST['pet-breed']
        pet_age = request.POST['pet-age']
        pet_weight = request.POST['pet-weight']
        uni_pk = request.POST['uni-pk']

        data = PetInfo(
            pet_name = pet_name,
            pet_breed = pet_breed,
            pet_age = pet_age,
            pet_weight = pet_weight,
            uni_pk=uni_pk,
        )
        data.save()
        return render(request, self.template_location)


@csrf_exempt
def symptom(request):

    problem = request.POST['problem']
    pet_key = request.POST['hidden-uni-pk']
    pet = PetInfo.objects.get(uni_pk=pet_key)

    sysmptom = PetSymptom(
        symptom_type = problem,
        pet = pet
    )
    sysmptom.save()
    return render(request, 'frontend/index.html')


class GetProductList(View):

    def get(self, request):
        data = Product.objects.all().values()
        return JsonResponse({'data': list(data)})

