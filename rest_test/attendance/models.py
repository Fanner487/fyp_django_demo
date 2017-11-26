# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Attendance(models.Model):
	event_name = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=True')
	organiser = models.CharField(max_length=255)
	scheduled = models.DateTimeField('date scheduled')
