from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'gateway'

urlpatterns = [
    path('private/', views.gateway_in_private),
    path('public/', views.gateway_in_public),
    path('gateway-test/', views.gateway_redirect_test),
    path('Oauth2test/', views.Oauth2test),
    path('love',views.love)
]