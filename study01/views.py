import requests
from django.shortcuts import render, HttpResponse, redirect
from numbmanage import models
from django import forms


# Create your views here.
def index(req):
    title = "孝子部落"
    return render(req, 'index.html')


class UserModelForm(forms.ModelForm):
    class Meta:
        models.Userlist
        fields = ["uname", "password", "name", "gender", "age", "depart", "grade"]


# class user_add:
#     form = UserModelForm()
#     return render(request, 'user_form_model_add')


from study01.models import UserInfo


# def user_list(req):
#     user_list = UserInfo.objects.all()
#     return render(req, "user_info.html", {"user_list": user_list})

def add_user(request):
    if request.method == "GET":
        return render(request, 'adduser.html')
    # 获取用户提交的数据
    user = request.POST.get("user")
    tel = request.POST.get("tel")
    account = request.POST.get("account")
    pwd = request.POST.get("pwd")

    # 将数据添加至数据库
    UserInfo.objects.create(name=user, tel=tel, account=account, password=pwd)

    # 添加成功后自动跳转页面
    return redirect('/user/')


def news(req):
    import requests
    res = requests.get("https://www.asmr.pw/api/fs/list")
    data_list = res.json()
    print(data_list)
    return render(req, 'news.html', {"name_list": data_list})


def test(req):
    print(req.POST)
    return redirect("http://www.baidu.com1")


def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    else:
        # print(req.POST)
        user_name = req.POST.get('user')
        password = req.POST.get('pwd')

        if user_name == 'root' and password == "123":
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")


# 部门列表
def depart_list(req):
    queryset = models.Department.objects.all()
    return render(req, 'depart_list.html', {'queryset': queryset})


# 部门添加
def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/list")


# 部门删除
def depart_del(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")


# 部门修改
def depart_edit(request, nid):
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,...]
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_object": row_object})
    # 获取用户提交修改的标题
    title = request.POST.get("title")
    # 根据ID找到数据库中的数据，并进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    # 提交成功后跳转页面
    return redirect("/depart/list")


# 分类添加
def class_add(request):
    if request.method == "GET":
        return render(request, 'class_add.html')
    cname = request.POST.get("cname")
    models.Class.objects.create(cname=cname)
    return redirect("/class/list")


# 分类删除
def class_del(request):
    nid = request.GET.get("nid")
    models.Class.objects.filter(id=nid).delete()
    return redirect("/class/list")


# 分类编辑
def class_edit(request, nid):
    if request.method == "GET":
        row_object = models.Class.objects.filter(id=nid).first()
        return render(request, "class_edit.html", {'row_object': row_object})
    cname = request.POST.get("cname")
    models.Class.objects.filter(id=nid).update(cname=cname)
    return redirect("/class/list")


# 部门列表
def class_list(request):
    classset = models.Class.objects.all()
    return render(request, 'class_list.html', {'class_list': classset})


def user_list(request):
    user_list = models.Userlist.objects.all()
    return render(request, 'user_list.html', {'userlist': user_list})
