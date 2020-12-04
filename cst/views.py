from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from cst import models
from django.views import View
import json
from django.core.paginator import EmptyPage, PageNotAnInteger
from cst.MyPaginator import MyPaginator


# Create your views here.

def show_student_table(request):
    """
    学生表 展示一下
    增加分页器
    :param request:
    :return:
    """

    test_list = []
    for i in range(10000):
        s = {"name": str(i) + "ks", "age": i}
        test_list.append(s)

    student_list = models.Student.objects.all().order_by("-id")  # 反向排序
    class_list = models.Class.objects.all()
    now_page = request.GET.get("p", 1)
    paginator = MyPaginator(now_page=now_page, max_display_page=11, object_list=student_list, per_page=10)

    try:
        page = paginator.page(int(now_page))
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)

    return render(request, "student.html", locals())




# def add_student(request):
#     """
#     增加学生信息
#     :param request:
#     :return:
#     """
#     class_list = models.Class.objects.all()
#     if request.method == "GET":
#         return render(request, "add_student.html", locals())
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         name_error = "姓名未输入!" if not name else ""
#         age = request.POST.get("age")
#         age_error = "年龄未输入! " if not age else ""
#         gender_s = request.POST.get("gender")
#         gender = "男性" if gender_s == "1" else "0"
#         phone = request.POST.get("phone")
#         phone_error = "电话未输入或超过长度11位 !" if not phone or len(phone) >= 12 else ""
#         choose_class = request.POST.get("choose_class")
#         is_ok = False
#         try:
#             models.Student.objects.create(
#                 name=name, age=age, gender=gender, phone_number=phone, student_class_id=choose_class
#             )
#             is_ok = True
#         except  Exception as e:
#             print("error-------", e)
#         return render(request, 'add_student.html', locals())

def add_student(request):
    """使用 ajax 来异步发送请求"""
    response = {"status": True, "Message": None, 'nid': None, 'alls': None}
    print(request.POST)
    try:
        name = request.POST.get("username")
        age = request.POST.get("age")
        gender = "男性" if request.POST.get("gender") == '1' else "女性"
        phone_number = request.POST.get("phone_number")
        class_id = request.POST.get("class")

        obj = models.Student.objects.create(
            name=name, age=age, gender=gender, phone_number=phone_number, student_class_id=class_id)
        response['Message'] = "成功"
        response["nid"] = obj.id
        response["alls"] = str(models.Student.objects.all().count())
        print(response)
    except Exception as e:
        response["status"] = False
        response["Message"] = "你输入的信息有误哦,请确保输入正确!"
        print(e)

    return HttpResponse(json.dumps(response, ensure_ascii=False))


# def del_student(request):
#     # 删除学生表
#     student_id = request.GET.get("nid")
#     models.Student.objects.filter(id=student_id).first().delete()
#     return HttpResponseRedirect(reverse("cst:student"))

def del_student(request):
    # ajax 删除学生信息
    response = {"status": True, "Message": None, "alls": None}
    try:
        nid = request.GET.get("nid")
        models.Student.objects.filter(id=nid).delete()
        response["Message"] = "ok"
        response["alls"] = str(models.Student.objects.all().count())
    except Exception as e:
        response["status"] = False
        response["Message"] = "删除学生信息错误"
        print(e)

    return HttpResponse(json.dumps(response, ensure_ascii=False))


def update_student(request):
    """
    ajax 进行数据更新 异步更新
    :param request:
    :return:
    """
    # TODO:  修复
    print(request.POST)
    # print(json.loads(request.POST.get("test"))['k'])  前端传入字符串 后端进行序列化转换为 字典对象然后取值
    response = {"status": True, "Message": None}
    try:
        nid = request.POST.get("edit_id")
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = "男性" if request.POST.get("gender") == "1" else "女性"
        phone_number = request.POST.get("phone_number")
        class_id = request.POST.get("class")
        models.Student.objects.filter(id=nid).update(
            name=username,
            age=age,
            gender=gender,
            phone_number=phone_number,
            student_class_id=class_id
        )
    except  Exception as e:
        response["status"] = False
        response["Message"] = "更新失败,请检查你输入的值."
        print(e)
    return HttpResponse(json.dumps(response, ensure_ascii=False))

# def update_student(request):
#     # 更新表
#     student_id = request.GET.get("nid")
#     if request.method == "GET":
#         student_info = models.Student.objects.filter(id=student_id).first()
#         class_list = models.Class.objects.all()
#         return render(request, "update_student.html", locals())
#     elif request.method == "POST":
#         # 根据id进行更新
#         student_id = request.POST.get("student_id")
#         name = request.POST.get("name")
#
#         age = request.POST.get("age")
#
#         gender_s = request.POST.get("gender")
#         gender = "男性" if gender_s == "1" else "0"
#         phone = request.POST.get("phone")
#
#         # phone_error = "电话未输入或超过长度11位 !" if not phone or len(phone) >= 12 else ""
#         choose_class = request.POST.get("choose_class")
#         print(student_id)
#         try:
#             models.Student.objects.filter(id=student_id).update(
#                 name=name, age=age, gender=gender, phone_number=phone, student_class_id=choose_class,
#             )
#             is_ok = "更新成功!"
#             print(name, age, gender, choose_class)
#         except Exception as e:
#             is_ok = e
#
#         return render(request, "update_student.html", locals())

