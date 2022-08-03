# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 19:28
# @Author  : xiaosong
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from appbackend.login import views

urlpatterns = [
    path('creatNewUser/', views.creatNewUser, name='creatNewUser'),  # 创建用户
    path('getVerifyCode/', views.getVerifyCode, name='getVerifyCode'),  # 获取验证码
    path('login/', views.authLogin, name='login'),  # 登录
    path('logout/', views.authLogout, name='logout')  # 登出
]
