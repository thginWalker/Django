# -*- coding: utf-8 -*-


from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
#奖罚管理
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from appraise.models import user,commit
from django.contrib import messages

#from django.forms.models import model_to_dict


#显示学生管理信息
def studentManage(request):
    list = user.objects.all()
    return render(request, 'appraise/student.html', {'contacts': list})

#学生新增信息
@csrf_exempt
def addStudent(request):
	if request.POST:
		username = request.POST['ausername']
		name = request.POST['aname']
		age = request.POST['aage']
		idnumber = request.POST['aidnumber']#登录角色
		sex = request.POST['asex']
		email = request.POST['aemail']
		result = user.objects.create(username = username, password = '123456', name = name, age = age, idnumber = idnumber, sex = sex ,email = email, flag = 2)
	list = user.objects.all()
	return render(request, 'appraise/student.html', {'contacts': list})

#学生更改信息
@csrf_exempt
def studentUpdate(request):
	if request.POST:
		id = request.POST['upid']
		username = request.POST['uusername']
		name = request.POST['uname']
		age = request.POST['uage']
		idnumber = request.POST['uidnumber']#登录角色
		sex = request.POST['usex']
		email = request.POST['uemail']
	update = user.objects.get(id=id)
	update.username = username
	update.name = name
	update.age = age
	update.idnumber = idnumber
	update.sex = sex
	update.email = email
	update.save()
	list = user.objects.all()
	return render(request, 'appraise/student.html', {'contacts': list})

#学生删除信息
@csrf_exempt
def studentDelete(request):
	if request.POST:
		id = request.POST['delid']
	result = user.objects.get(id = id)
	result.delete()
	list = user.objects.all()
	return render(request, 'appraise/student.html', {'contacts': list})

#显示奖罚管理信息
def sanctionManage(request):
	list = commit.objects.all()
	result = []
	name = []  
	for obj in list:
		result.append(obj.user)
	for var in result:
		data = user.objects.get(id = var).name
		name.append(data)
	i = 0
	for obj in list:
		obj.name = name[i]
		i = i + 1
	userdata = user.objects.all()
	#输出调试 
	return render(request, 'appraise/sanction.html', {'contacts': list,'name':name,'user':userdata})

#更改密码跳转
def changePassword(request):
	return render(request, 'appraise/chanpas.html')

def passwordConfirm(request):
	if request.POST:
		ancent = request.POST['ancent']
		update = request.POST['update']
		#confirm = request.POST['confirm']
	name = request.session.get('key')
	result = user.objects.get(username = name,password = ancent,flag = 0)
	id = result.id
	if result:
		modify = user.objects.get(id=id)
		modify.password = update
		modify.save()
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'appraise/chanpas.html')



#更改信息

def changeMessage(request):
	name =request.session.get('key')
	result = user.objects.get(username = name,flag = 0)
	return render(request, 'appraise/chanmes.html',{'contacts': result}) 

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
	result = user.objects.get(username = keyName,flag = 0)
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
		list = user.objects.get(username = keyName,flag = 0)
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'appraise/chanmes.html',{'contacts': list})