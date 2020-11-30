# -*- coding :  utf-8 -*-
# @Time      :  2020/11/21  14:27
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
from django.urls import path
from app02 import views

app_name = "app02"

urlpatterns = [
    path('testform.html', views.testform, name='testform'),
    path("getdata/", views.getdata, name="getdata"),
]
