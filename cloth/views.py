from django.shortcuts import render
from . import models
from django. views import View


class AllClothView(View):
    def get(self, request):
        cloth = models.cloth.objects.all().order_by('-id')
        return render(request, 'cloth/all_cloth.html', {'cloth': cloth})


class MaleClothView(View):
    def get(self, request):
        male = models.cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
        return render(request, 'cloth/male.html', {'male': male})


class FemaleClothView(View):
    def get(self, request):
        female = models.cloth.objects.filter(tags__name='женская одежда').order_by('-id')
        return render(request, 'cloth/female.html', {'female': female})


class KidsClothView(View):
    def get(self, request):
        kids = models.cloth.objects.filter(tags__name='детская одежда').order_by('-id')
        return render(request, 'cloth/kids.html', {'kids': kids})



# def all_cloth(request):
#     if request.method == 'GET':
#         cloth = models.cloth.objects.filter().order_by('-id')
#         return render(request, template_name='cloth/all_cloth.html',
#                       context={'cloth': cloth})

# def male_cloth(request):
#     if request.method == 'GET':
#         male = models.cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
#         return render(request, template_name='cloth/male.html',
#                       context={'male': male})

# def female_cloth(request):
#     if request.method == 'GET':
#         female = models.cloth.objects.filter(tags__name='женская одежда').order_by('-id')
#         return render(request, template_name='cloth/female.html',
#                       context={'female': female})

# def kids_cloth(request):
#     if request.method == 'GET':
#         kids = models.cloth.objects.filter(tags__name='детская одежда').order_by('-id')
#         return render(request, template_name='cloth/kids.html',
#                       context={'kids': kids})
