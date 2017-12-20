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
    list = user.objects.filter(flag = 2)
    return render(request, 'advisers/student.html', {'contacts': list})



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
	#输出调试 
	return render(request, 'advisers/sanction.html', {'contacts': list})

#通过审核
@csrf_exempt
def sanctionConfirmy(request):
	if request.POST:
		id = request.POST['sanidy']
	modify = commit.objects.get(id=id)
	modify.examine = 1
	modify.save()
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
	#输出调试 
	return render(request, 'advisers/sanction.html', {'contacts': list})

#否决审核
@csrf_exempt
def sanctionConfirmn(request):
	if request.POST:
		id = request.POST['sanidn']
	modify = commit.objects.get(id=id)
	modify.examine = 2
	modify.save()
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
	#输出调试 
	return render(request, 'advisers/sanction.html', {'contacts': list})

#更改密码跳转
def changePassword(request):
	return render(request, 'advisers/chanpas.html')

def passwordConfirm(request):
	if request.POST:
		ancent = request.POST['ancent']
		update = request.POST['update']
		#confirm = request.POST['confirm']
	name = request.session.get('key')
	#return HttpResponse(ancent)
	try:
		result = user.objects.get(name = name,password = ancent,flag = 1)
		id = result.id
	except:
		pass
	if result:
		modify = user.objects.get(id=id)
		modify.password = update
		modify.save()
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'advisers/chanpas.html')



#更改信息
def changeMessage(request):
	name =request.session.get('key')
	result = user.objects.get(name = name,flag = 1)
	return render(request, 'advisers/chanmes.html',{'contacts': result}) 

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
	result = user.objects.get(name = keyName,flag = 1)
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
		list = user.objects.get(name = keyName,flag = 1)
		messages.error( request, '修改成功!', extra_tags='bg-warning text-warning')
	else:
		messages.error( request, '修改失败!', extra_tags='bg-warning text-warning')
	return render(request, 'advisers/chanmes.html',{'contacts': list})

