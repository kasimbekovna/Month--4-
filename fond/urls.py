from django.urls import path
from . import views

app_name = 'fond'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('fond_list/', views.UserListView.as_view(), name='user_list'),
]