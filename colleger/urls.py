# -*- coding: utf-8 -*-
from django.conf.urls import url
#from . import views
import views
 
urlpatterns = [
	url(r'^student/',views.studentManage),
	url(r'^chanpas/',views.changePassword),
	url(r'^chanmes/',views.changeMessage),
]


