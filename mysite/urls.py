# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from . import view


 
urlpatterns = [
	url(r'^$', view.index),
	url(r'^login/', view.login),
	url(r'^register/',view.register),
	url(r'^logout/',view.logout),
	url(r'^appraise/',include("appraise.urls")),
	url(r'^advisers/',include("advisers.urls")),
	url(r'^colleger/',include("colleger.urls")),

]
