from .models import Traffic, Location, heading
from rest_framework import serializers

class TrafficSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Traffic
		fields = ['lightValue', 'lightColor',]


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ['lat', 'lon', 'latD', 'lonD','heading']


class HeadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = heading
		fields = ['heading',]