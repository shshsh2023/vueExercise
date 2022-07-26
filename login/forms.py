# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 19:43
# @Author  : xiaosong
# @File    : forms.py
# @Software: PyCharm
from django import forms


class loginForm(forms.Form):
    username = forms.CharField(label='用户名', min_length=5, max_length=10, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control rounded mb-1',
            'id': "username",
            'placeholder': "Username",
            'name': "username",
        }), )
    password = forms.CharField(label='密码', min_length=5, max_length=10, widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control rounded',
            'id': "password",
            'placeholder': "Password",
            'name': "password",
        }), error_messages={"min_length": "你太短了", "required": "该字段不能为空！"})
