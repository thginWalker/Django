# -*- coding: utf-8 -*-


from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
#奖罚管理
from django.shortcuts import render
from django.views.decorators import csrf
from appraise.models import admin,commit

 
def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'appraise/login.html', context)

def login(request):
	ctx = {}
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		role = request.POST['role']#登录角色
	#登录验证
	
	result = admin.objects.filter(username = username,password = password,flag = 2)
	if result:
		#比较成功，跳转index
		return render(request,"appraise/index.html")
	else:
		#比较失败，还在login
		return render(request,"appraise/login.html")
	
	

def studentManage(request):
    list = admin.objects.all()
    return render(request, 'appraise/student.html', {'contacts': list})


def sanctionManage(request):
    list1 = commit.objects.all()
    return render(request, 'appraise/sanction.html', {'contacts': list1})