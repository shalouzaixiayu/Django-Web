from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views import View
import json
from django.views.decorators.clickjacking import xframe_options_exempt  # iframe拒绝问题
from teacher_student_class.settings import MEDIA_ROOT


# Create your views here.
# @xframe_options_exempt
class Ajax(View):
    def get(self, request):
        print(request.POST)
        print(request.GET)
        return HttpResponse(json.dumps("get提交过来的", ensure_ascii=False))

    def post(self, request):
        ret = {"status": True, "message": "post提交过来的. 我们需要在setting中修改一下文件, 解决一下跨域问题 " + request.POST.get("ts")}
        print(request.POST)
        print(request.GET)
        return HttpResponse(
            json.dumps(ret, ensure_ascii=False))


# @xframe_options_exempt
class TestAjax(View):
    def get(self, request):
        return render(request, 'testajax.html', locals())

    def post(self, request):
        return HttpResponse(json.dumps("yes, you like me,", ensure_ascii=False))


def AjaxFile(request):
    if request.method == "POST":
        #  进行文件的传输  使用 fromdata 进行
        print(request.GET)
        print(request.POST)
        print(request.POST.get("message"))
        # print(request.FILES.get("image1"))
        print(request.FILES)
        print(request.FILES.get("image2"))
        # for i in request.FILES.get("image2").chunks():
        #     print(i)

        return HttpResponse("...")
    else:
        return HttpResponseRedirect("http://www.baidu.com")
