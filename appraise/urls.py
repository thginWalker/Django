# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

 
urlpatterns = [
    url(r'^$', views.index),
	url(r'^login/',views.login),
	url(r'^student/',views.studentManage),
	url(r'^sanction/',views.sanctionManage)

]


