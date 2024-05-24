from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.AllClothView.as_view(), name='all_cloth'),
    path('male/', views.MaleClothView.as_view(), name='male'),
    path('female/', views.FemaleClothView.as_view(), name='female'),
    path('kids/', views.KidsClothView.as_view(), name='kids'),
]