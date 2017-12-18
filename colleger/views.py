# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
#奖罚管理
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from appraise.models import user,commit
from django.contrib import messages


#显示个人奖罚信息
def studentMassage(request):
	keyName = request.session.get('key')
	result = user.objects.get(name = keyName,flag = 2)#学生
	id = result.id
	list = commit.objects.filter(user = id)
	return render(request, 'colleger/student.html', {'contacts': list})


#更改密码跳转
def changePassword(request):
	return render(request, 'colleger/chanpas.html') 

#确定更改密码
def passwordConfirm(request):
	if request.POST:
		ancent = request.POST['ancent']
		update = request.POST['update']
		#confirm = request.POST['confirm']
	name = request.session.get('key')
	result = user.objects.get(name = name,password = ancent,flag = 2)
	id = result.id
	if result:
		modify = user.objects.get(id=id)
		modify.password = update
		modify.save()
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'colleger/chanpas.html')



#更改信息
def changeMessage(request):
	name =request.session.get('key')
	result = user.objects.get(name = name,flag = 2)
	return render(request, 'colleger/chanmes.html',{'contacts': result}) 

@csrf_exempt
def messageConfirm(request):
	if request.POST:
		username = request.POST['username']
		name = request.POST['name']
		age = request.POST['age']
		idnumber = request.POST['idnumber']
		sex = request.POST['sex']
		email = request.POST['email']
	keyName = request.session.get('key')
	result = user.objects.get(name = keyName,flag = 2)
	id = result.id
	if result:
		modify = user.objects.get(id=id)
		modify.username = username
		modify.name = name
		modify.age = age
		modify.idnumber = idnumber
		modify.sex = sex
		modify.email = email
		modify.save()
		list = user.objects.get(name = keyName,flag = 2)
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'colleger/chanmes.html',{'contacts': list})


