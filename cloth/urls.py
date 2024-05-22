from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.all_cloth, name='all_cloth'),
    path('male/', views.male_cloth, name='male'),
    path('female/', views.female_cloth, name='female'),
    path('kids/', views.kids_cloth, name='kids'),
]