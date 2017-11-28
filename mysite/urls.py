# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from . import view

import appraise.views as bv
 
urlpatterns = [
    url(r'^hello$', view.hello),
	url(r'^appraise/',include("appraise.urls")),
#	url(r'^static/(?P<path>.*)$', 'assets',{ 'document_root': settings.STATIC_URL }),
]
