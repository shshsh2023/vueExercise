import datetime
import traceback

import django.db.utils
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from login.forms import loginForm

from django.contrib.auth.models import User
from django.http import HttpResponse
from login.models import UserExtension


# Create your views here.
@csrf_exempt
def creatNewUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        email = request.POST['email']
        verifyCode = request.POST['verifyCode']
        age = request.POST['age']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            # 给扩展的字段设置值
            UserExtension.objects.filter(user_id=user.id).update(age=age, sex=sex, birthday=birthday)
            # 更改调用 user.save()
            return HttpResponse('1')
        except django.db.utils.IntegrityError:
            traceback.print_exc()
            return HttpResponse('用户已存在')
    return HttpResponse(0)


# 获取验证码
@csrf_exempt
def getVerifyCode(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
    return HttpResponse(1)
