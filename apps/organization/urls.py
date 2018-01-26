# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-25 下午3:47"

from django.conf.urls import url, include

from django.conf.urls import url, include
from .views import OrgView,AddUserAskView

urlpatterns = [
    #课程机构首页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$',AddUserAskView.as_view(), name="add_ask"),
]