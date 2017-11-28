# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
 
def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'appraise/index.html', context)

def login(request):
	ctx = {}
	if request.POST:
		ctx['username'] = request.POST['username']
	return render(request,"appraise/post.html",ctx)