from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import fields, widgets  # 这二个都继承自 forms  可以不额外导入这个二个库的使用
import json
from django.utils.safestring import mark_safe  # 将 string  加工成 html 文档 返回到页面,进行渲染
from cst import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from teacher_student_class.settings import MEDIA_ROOT


class MyForms(forms.Form):
    """
    规定一些参数的限制性
    """
    name = forms.CharField(label='My name', max_length=10, required=True,
                           label_suffix="-->")
    passwd = forms.CharField(min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'form-control', "style": "width:100px;height:25px;", "autocomplete": ""}))
    email = forms.EmailField(required=True, error_messages={"invalid": "其他错误", })
    age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"style": "width:100px;height:25px;",
                                                                          'class': "form-control"}))
    file = forms.FileField(required=True, label="FILE")

    # 单选框
    sex = forms.ChoiceField(
        label="Sex",
        initial=1,
        choices=[(1, "男"), (2, "女")],
        widget=forms.RadioSelect(),  # 标签类型

    )
    # 下拉框
    area = forms.ChoiceField(
        label="Area",
        initial=1,
        choices=[(1, "北京"), (2, "上海"), (3, "深圳")],
        widget=forms.Select)
    # 多选下拉框
    author = forms.MultipleChoiceField(
        label="Author : ",
        initial=1,
        choices=[(1, "张山"), (2, "李四")],
        widget=forms.SelectMultiple,  # 标签类型
    )
    # 单选的方框

    keep = forms.ChoiceField(
        label="If keep/No",
        choices=((True, 1), (False, 2)),
        # initial=1,
        widget=forms.CheckboxInput,  # 标签类型

    )
    # 静态字段 进行数据库的动态更新

    # print(models.Student.objects.all().values_list('id', 'name'))
    stu = forms.ChoiceField(
        label="学生",
        choices=models.Student.objects.all().values_list('id', "name"),
        widget=forms.Select,
    )
    # 用自带的模板更新 Field 只能做到数据库的自动更新， 但是其他功能不行， 比如id的获取， 显示问题
    # 封装性太强，不行， 需要自定义
    stu1 = forms.ModelChoiceField(

        label="学生",
        queryset=models.Student.objects,
    )

    # 多选的方框  使用  MultipleChoiceField
    hobby = forms.TypedMultipleChoiceField(
        coerce=lambda x: int(x),  # 使用 Type.....   加上类型规则, 就可以获得需求的类型值
        # lambda x:float(x) char(x) 都可以
        label="Your love ",
        choices=[(1, "看书",), (2, "写作业"), (3, "睡觉"), ],
        widget=forms.CheckboxSelectMultiple,
    )
    # 时间类型
    import time
    date = forms.CharField(
        label="Now time",
        initial=time.strftime("%Y-%m-%d", time.localtime()),
        # initial='1999-10-20',  # 时间格式
        widget=forms.TextInput(attrs={"type": "date"})
    )

    # 文本域
    YourTip = forms.CharField(
        label="Your Tip : ",
        initial="",
        widget=forms.Textarea(attrs={"class": "form-control", "style": "height:100px;width:200px;",
                                     "placeholder": "如果你有建议, 你可以在这里畅所欲言!"}),
    )

    # s = forms.ModelChoiceField()
    # Create your views here.
    def __init__(self, *args, **kwargs):
        """
        进行数据的更新.  之前我们定义在外围的都是静态字段, 当程序运行的时候, 那
        些字段从上到下加载到内存中,   成为了一个固定的值, 所以我们让页面刷新的时候
        这些值也不会发生变化,  所以我们不能动态的进行改变,
        在这里, 我们构造一个初始化方式,  继承 父类的 __init__ , 在这个方法中, 我们进行数据
        的更新, 这样就可以达到动态的更新了.
        这就是每一次 obj 请求这个对象, 那么对象就会自动执行这个构造方法, 自动的取一次,
        刷新一次取一次
        :param args:    可迭代的类型
        :param kwargs:    字典类型
        """
        super().__init__(*args, **kwargs)
        self.fields["stu"].choice = models.Student.objects.all().values_list('id', 'name')

    def clean_name(self):
        """
        对数据进行额外处理， 扩展form中的 clean_%s  方式
        如果数据正确， 不重复, 直接返回cleaned_data
        如果数据不正确  重复.  抛出异常 ValidationError
        :return:
        """
        name_date = self.cleaned_data["name"]
        if models.Student.objects.filter(name=name_date).count():
            #  如果重复，抛出异常
            raise ValidationError("用户名已重复!", code="invalid")
        return name_date

    def clean(self):
        name_date = self.cleaned_data
        s = name_date.get("name")
        if s:
            raise ValidationError("整体错误了")
        return self.cleaned_data


def testform(request):
    if request.method == "GET":
        # obj = MyForms({"name":"superman"}) 初始化默认值
        obj = MyForms()
        return render(request, 'testform.html', locals())
    else:

        obj = MyForms(request.POST, request.FILES)
        if obj.is_valid():
            s = obj.cleaned_data
            print(s)
            return HttpResponseRedirect("http://www.baidu.com")
        else:
            return render(request, 'testform.html', locals())


from django.core.serializers import serialize


def getdata(request):
    """
    二种序列化的方式都可以， 如果返回所有对象 all ， 就要使用django内置的
    serialize 序列化， 将 queryfield 转换为 字符串， 然后在经过json转换一下到前端，
    最后前端经过二次反序列化，就可以拿到对象，
    在这里，  data被序列化了2次，  status 被序列化了1次
    前端反序列化的时候， 也是同样的次数

    如果不直接拿数据， 而是用  values 去取一些数据，那么我们要把取出来的  querylist 转换为
    list 类型， 然后再经过 json进行序列化操作， 传到前端， 但是前端这个时候， 只是需要经过一次
    反序列化就可以拿到data对象了，  不需要这么麻烦，

    区别，   直接拿到所有的数据 all  需要使用django内置的函数进行额外的序列化， 前端需要进行二次反序列化
            只拿一部分数据 values   需要将 querylist转换为 list 对象，  前端只需要进行一次反序列化

    :param request:
    :return:
    """
    ret = {"status": True, "data": None}
    try:
        user_list = models.Student.objects.all()
        ret["data"] = serialize("json", user_list)
    except Exception as e:
        ret["status"] = False
    return HttpResponse(json.dumps(ret))

    # def getdata(request):
    #     ret = {"status": True, "data": None}
    #     try:
    #         user_list = models.Student.objects.all().values("id", "name")
    #         ret["data"] = list(user_list)
    #     except Exception as e:
    #         ret["status"] = False
    #     return HttpResponse(json.dumps(ret))


from os import path


def getfile(request):
    """
    将页面中上传的文件， 导入数据库中。
    实现数据的下载
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "getfile.html", locals())
    else:
        text = request.POST.get("text")
        img = request.FILES.get("img")
        with open(path.join(MEDIA_ROOT, img.name), 'wb') as fw:
            for line in img.chunks():
                fw.write(line)
            print("ok")
        return HttpResponse(json.dumps(text, ensure_ascii=False))
