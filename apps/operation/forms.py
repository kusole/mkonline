# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-25 下午3:36"
from django import forms
from operation.models import UserAsk


# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=50)
#

class UserAskForm(forms.ModelForm):

    class Meta:
        model=UserAsk
        fields = ['name','mobile','course_name']
