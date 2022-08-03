# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 14:35
# @Author  : xiaosong
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from appbackend.verifications import views

urlpatterns = [
    path('returnImageVerifyCode/', views.returnImageVerifyCode, name='returnImageVerifyCode')  # 返回验证码
]
