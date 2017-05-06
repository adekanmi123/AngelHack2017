from .models import Traffic, Location
from rest_framework import serializers

class TrafficSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Traffic
		fields = ['lightValue', 'lightColor',]


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ['lat', 'lon',]