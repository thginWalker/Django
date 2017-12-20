from __future__ import unicode_literals

import json
from django.db import models
#from appraise.models import commit,user

class user(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	name = models.CharField(max_length=32)
	age = models.IntegerField()
	idnumber = models.CharField(max_length=32)
	sex = models.IntegerField()
	email = models.CharField(max_length=18)
	flag = models.IntegerField()
	remark = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name


class commit(models.Model):
	user = models.IntegerField()
	category = models.IntegerField()
	level = models.IntegerField()
	reason = models.CharField(max_length=18)
	date = models.CharField(max_length=28)
	examine = models.IntegerField()
	remark = models.CharField(max_length=50)
	def __unicode__(self):
		return self.user

