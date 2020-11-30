# -*- coding :  utf-8 -*-
# @Time      :  2020/11/11  21:08
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
"""class_student_teachers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cst import views

# 别名
app_name = "cst"

urlpatterns = [
    path("student.html", views.show_student_table, name="student"),
    path("add_student.html", views.add_student, name="add_student"),
    path("del_student.html", views.del_student, name="del_student"),
    path("update_student.html", views.update_student, name="update_student"),
]
