from django.shortcuts import render
import json
import requests


# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import GatewayForm
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser


def gateway_in_public(request):
    if request.method == "POST":
        print("recieve post")
        data =request.POST  #POST 大写
        print(data)
        api = eval(data['type'])
        print(api)
        biz_data = data['biz_data']
        print(biz_data)
        #url = 'http://127.0.0.1:8000/userprofile/{}/'.format(api)
        #print(url)
        #response = requests.post(url = url,data= eval(biz_data))   #这里要用eval将字符串转成一个json格式的data
        return HttpResponse("you are request API {}".format(api))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gateway_in_private(request):
    if request.method == "POST":
        print("recieve post")
        data =request.POST  #POST 大写
        print(data)
        api = eval(data['type'])
        print(api)
        biz_data = data['biz_data']
        print(biz_data)
        #url = 'http://127.0.0.1:8000/userprofile/{}/'.format(api)
        #print(url)
        #response = requests.post(url = url,data= eval(biz_data))   #这里要用eval将字符串转成一个json格式的data
        return HttpResponse("you are request API {}".format(api))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Oauth2test(request):
    data = request.POST
    #print(data)
    username = data['username']
    #print(request.auth)
    #print(request.user)
    #print(username)
    if request.user.username == username:
        return HttpResponse("success")

def gateway_redirect_test(request):
    if request.method == "POST":
        data=request.POST  #POST 大写
        print(data)
        print("success")
        return HttpResponse("redirect test success")

def love(request):
    return render(request, 'gate/yes.html',{
            'url': "eat.png",
        })
