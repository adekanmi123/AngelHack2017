# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Traffic(models.Model):
	LIGHT = (
		('R', 'red'),
		('Y', 'yellow'),
		('G', 'green'),
		)
	area = models.CharField(default="New Delhi", max_length=40,)
	lightValue = models.IntegerField()
	lightColor = models.CharField(max_length=1, choices=LIGHT,)

	def __str__(self):
		return self.area

class Location(models.Model):
	lat = models.DecimalField(max_digits=15, decimal_places=10)
	lon = models.DecimalField(max_digits=25, decimal_places=10)
	area = models.CharField(default="New Delhi", max_length=40,)
