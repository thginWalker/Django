# -*- coding: utf-8 -*-
from django.conf.urls import url
#from . import views
import views
 
urlpatterns = [
	url(r'^student/',views.studentManage),
	url(r'^stuadd/',views.addStudent),
	url(r'^stupdate/',views.studentUpdate),
	url(r'^studel',views.studentDelete),
	url(r'^sanction/',views.sanctionManage),
	url(r'^chanpas/',views.changePassword),
	url(r'^pasconfirm/',views.passwordConfirm),
	url(r'^chanmes/',views.changeMessage),
	url(r'^mesconfirm/',views.messageConfirm),
]


