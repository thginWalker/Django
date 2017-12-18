# -*- coding: utf-8 -*-
from django.conf.urls import url
import views
 
urlpatterns = [
	url(r'^student/',views.studentManage),
	url(r'^sanction/',views.sanctionManage),
	url(r'^sanconfirmy/',views.sanctionConfirmy),
	url(r'^sanconfirmn/',views.sanctionConfirmn),
	url(r'^chanpas/',views.changePassword),
	url(r'^pasconfirm/',views.passwordConfirm),
	url(r'^chanmes/',views.changeMessage),
	url(r'^mesconfirm/',views.messageConfirm),
]


