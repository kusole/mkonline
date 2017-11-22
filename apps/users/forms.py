# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-22 下午1:17"

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5,max_length=16)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5,max_length=16)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
