# from django.db import models
from django import forms
from django.contrib.auth.models import User

# meta class
# meta data(메타데이터) : 데이터의 데이터

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# 로그인 품(아이디 비밀번호만 입력받아 처리)
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
