# -*- coding: utf-8 -*-


from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
#奖罚管理
from django.shortcuts import render
from django.views.decorators import csrf
from appraise.models import user,commit

#from django.forms.models import model_to_dict


#显示学生管理信息
def studentManage(request):
    list = user.objects.all()
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
def sanctionConfirmy(request):
	if request.POST:
		id = request.POST['sanidy']
		examine = request.POST['examiney']
	return HttpResponse(id)
	modify = commit.objects.get(id=id)
	modify.examine = examine
	modify.save()
	sanctionManage(request)

#否决审核
def sanctionConfirmn(request):
	if request.POST:
		id = request.POST['sanidn']
		examine = request.POST['examinen']
	modify = commit.objects.get(id=id)
	modify.examine = examine
	modify.save()
	sanctionManage(request)

#更改密码跳转
def changePassword(request):
	return render(request, 'advisers/chanpas.html') 


#更改信息
def changeMessage(request):
	return render(request, 'advisers/chanmes.html') 


