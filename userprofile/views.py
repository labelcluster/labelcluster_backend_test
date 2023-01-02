from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
#from .forms import ProfileForm
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def user_info(request):  #1002
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        user = User.objects.get(username=username)
        res = {"user_id":"{}".format(user.id),
               "last_login":"{not apply}",
               "is_staff":"{}".format(user.is_staff),
               "is_active":"{}".format(user.is_active),
               "email":"{}".format(user.email),
               "first_name":"{}".format(user.first_name),
               "last_name":"{}".format(user.last_name),
               "date_joined":"{}".format(user.date_joined)}
        js = json.dumps(res)
        print(js)
        return HttpResponse(js)

def user_login(request): #1001
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                accesscode = get_tokens_for_user(user)
                print(accesscode)
                return HttpResponse(json.dumps(accesscode))
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        return HttpResponse("请使用POST请求数据")

def user_register(request):   #1000接口
    if request.method == 'POST':
        # data = request.POST
        # print(data)
        # username = data['username']
        # email = data['email']
        # password1 = data['password1']
        # password2 = data['password2']
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username)
        print(password1)
        if password1 == password2:
            newUser = User()  #User 是model里面的
            newUser.username = username
            newUser.set_password(password1)
            newUser.email = email
            newUser.save()
            user = User.objects.get(username=username)
            accesscode = get_tokens_for_user(user)
            #res = {"user_id":"{}".format(user.id)}
            js = json.dumps(accesscode)
            #print(js)
            return HttpResponse(js)  #返回userid
            print("register success")
        else:
            return HttpResponse("密码不一致")

def profile_edit(request):
    if request.method == 'POST':
        data = request.POST
        key = data['user_id']
        updateUser = get_object_or_404(User, pk=key)
        if data['username']:
            updateUser.username = data['username']
        if data['password']:
            updateUser.set_password(data['password'])
        if data['email']:
            updateUser.email = data['email']
        if data['first_name']:
            updateUser.first_name = data['first_name']
        if data['last_name']:
            updateUser.last_name = data['last_name']

        # Edge case not checked yet
        updateUser.save()
        return HttpResponse("Success")



