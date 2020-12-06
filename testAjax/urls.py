# -*- coding :  utf-8 -*-
# @Time      :  2020/12/5  18:00
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
from testAjax import views
from django.urls import path

app_name = "testajax"
urlpatterns = [
    path("TestAjax.html", views.TestAjax.as_view(), name="TestAjax"),
    path("Ajax.html", views.Ajax.as_view(), name="Ajax"),
    path("AjaxFile.html", views.AjaxFile,)
]
