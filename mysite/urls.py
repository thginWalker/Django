# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from . import view


 
urlpatterns = [
    url(r'^hello$', view.hello),
	url(r'^appraise/',include("appraise.urls")),

]
