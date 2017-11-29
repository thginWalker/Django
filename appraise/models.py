from __future__ import unicode_literals

from django.db import models

class admin(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	age = models.IntegerField()
	idnumber = models.CharField(max_length=32)
	sex = models.IntegerField()
	email = models.CharField(max_length=18)
	flag = models.IntegerField()
	remark = models.CharField(max_length=50)
	
class commit(models.Model):
	category = models.IntegerField()
	level = models.IntegerField()
	reason = models.CharField(max_length=18)
	date = models.IntegerField()
	remark = models.CharField(max_length=50)
