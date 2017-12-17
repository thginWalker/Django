
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from appraise.models import user
 

	
#登录跳转函数
def index(request):
	return render(request, 'login.html')

#登录函数
def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		role = request.POST['role']#登录角色
	
	#登录验证 0管理员 1老师 2学生
	if role == '0':
		#return HttpResponse("Hello world ! ")
		result = user.objects.get(username = username,password = password,flag = 0)
		if result:
			#比较成功，跳转index
			request.session['key'] = result.name
			return render(request,"appraise/index.html")
		else:
			#比较失败，还在login
			return render(request,"login.html")
	elif role == '1':
		result = user.objects.get(username = username,password = password,flag = 1)
		if result:
			#比较成功，跳转index
			request.session['key'] = result.name
			return render(request,"advisers/index.html")
		else:
			#比较失败，还在login
			return render(request,"login.html")
	elif role == '2':
		result = user.objects.get(username = username,password = password,flag = 2)
		if result:
			#比较成功，跳转index
			request.session['key'] = result.name
			return render(request,"colleger/index.html")
		else:
			#比较失败，还在login
			return render(request,"login.html")
	else:
		return render(request,"login.html")

#注册功能
def register(request):
	if request.POST:
		username = request.POST['rusername']
		password = request.POST['rpassword']
		email = request.POST['remail']
	result = user.objects.create(username = username, password = password,email = email, flag = 2)
	list = user.objects.all()
	return render(request, 'login.html')

#退出登录
def logout(request):
	del request.session['key']
	return render(request, 'login.html')  

