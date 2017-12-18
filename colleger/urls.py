# -*- coding: utf-8 -*-
from django.conf.urls import url
#from . import views
import views
 
urlpatterns = [
	url(r'^message/',views.studentMassage),
	url(r'^chanpas/',views.changePassword),
	url(r'^pasconfirm/',views.passwordConfirm),
	url(r'^chanmes/',views.changeMessage),
	url(r'^mesconfirm/',views.messageConfirm),
]


