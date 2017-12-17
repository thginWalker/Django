# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
#奖罚管理
from django.shortcuts import render
from django.views.decorators import csrf
from appraise.models import user,commit

#from django.forms.models import model_to_dict


#显示个人奖罚信息
def studentManage(request):
    list = user.objects.all()
    return render(request, 'colleger/student.html', {'contacts': list})


#更改密码跳转
def changePassword(request):
	return render(request, 'colleger/chanpas.html') 


#更改信息
def changeMessage(request):
	return render(request, 'colleger/chanmes.html') 


