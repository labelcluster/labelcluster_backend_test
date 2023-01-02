
from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('1002/', views.user_info, name = 'user_info'),
    path('1001/', views.user_login, name='login'),
    path('1000/', views.user_register, name = 'register'),
    path('1004/', views.profile_edit, name='edit'),
]