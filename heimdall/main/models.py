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

	DIRECTION = (
		(1, 'forward'),
		(2, 'backward'),
		(3, 'left'),
		(4, 'right'),
		)
		
	lightValue = models.IntegerField(choices=DIRECTION)
	lightColor = models.CharField(max_length=1, choices=LIGHT,)


class Location(models.Model):
	lat = models.DecimalField(max_digits=15, decimal_places=10)
	lon = models.DecimalField(max_digits=15, decimal_places=10)
	latD = models.DecimalField(max_digits=15, decimal_places=10,)
	lonD = models.DecimalField(max_digits=15, decimal_places=10,)

