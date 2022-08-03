import json
import random
import smtplib
import traceback

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from appbackend.login.models import UserExtension


# Create your views here.
# 生成六位数字验证码
def generateVerifyCode():
    verifyCode = ''
    for i in range(6):
        verifyCode += str(random.randint(0, 10))
    cache.set('verifyCode', verifyCode, 60 * 10)
    verifyCodeMsg = '你的验证码为:' + verifyCode + ',十分钟内有效!'
    return verifyCodeMsg


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
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        if password != re_password:
            return HttpResponse('两次密码不相同')
        try:
            if verifyCode == cache.get('verifyCode'):
                cache.delete('verifyCode')
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=firstName, last_name=lastName)
                # 给扩展的字段设置值
                UserExtension.objects.filter(user_id=user.id).update(age=age, sex=sex, birthday=birthday)
                # 更改调用 user.save()
                return HttpResponse('注册成功')
            else:
                return HttpResponse('验证码错误')
        except:
            traceback.print_exc()
            return HttpResponse('0')
    return HttpResponse(0)


# 获取验证码
@csrf_exempt
def getVerifyCode(request):
    if request.method == 'POST':
        # 前端传来的是字符串
        body = json.loads(request.body)
        email = body['email']
        recipient_list = [email]
        try:
            verifyCodeMsg = generateVerifyCode()
            send_mail('注册验证码', verifyCodeMsg, None, recipient_list, False)
            return HttpResponse('验证码发送成功')
        except smtplib.SMTPException:
            traceback.print_exc()
            return HttpResponse('验证码发送失败')
    return HttpResponse(0)


# 登录
@csrf_exempt
def authLogin(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body['username']
        password = body['password']
        code = body['code']
        try:
            if code == cache.get('imageVerifyCode').lower():
                cache.delete('imageVerifyCode')
                authUser = authenticate(username=username, password=password)
                if authUser is not None:
                    login(request, authUser)
                    request.session['username'] = username
                    request.session['is_login'] = True
                    return HttpResponse('登录成功')
                else:
                    return HttpResponse('登录失败')
            else:
                return HttpResponse('验证码错误')
        except AttributeError:
            return HttpResponse('刷新验证码')
    return HttpResponse('登录失败')


# 登出
@csrf_exempt
def authLogout(request):
    if request.method == 'POST':
        request.session.flush()
        logout(request)
        return HttpResponse('注销成功')
    return HttpResponse('0')
