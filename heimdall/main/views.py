# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# from django.http import HttpResponse,JsonResponse
# from rest_framework.renderers import JSONRenderer

# from rest_framework.parsers import JSONParser

from rest_framework import generics
# Create your views here.
from .models import Traffic, Location, heading
from .serializers import TrafficSerializer, LocationSerializer, HeadingSerializer

# creating an endpoint for the root of our api

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'traffic':reverse('traffic-list', request=request, format=format),
# 		'location' : reverse('location-list', request=request, format=format),
# 		})


class LocationView(generics.ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class TrafficView(generics.ListCreateAPIView):
	queryset = Traffic.objects.all()
	serializer_class = TrafficSerializer


class TrafficDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Traffic.objects.all()
	serializer_class = TrafficSerializer


# for sending values to the index.html
def SendValue(request):
	# stuff = Location.objects.all()
	stuff = get_object_or_404(Location)
	lonD = stuff.lonD;
	latD = stuff.latD;
	lat =  stuff.lat;
	lon = stuff.lon;
	queryset = {
		'lonD' : lonD,
		'latD' : latD,
		'lat'  : lat,
		'lon'  : lon,
	}
	return render(request, "index.html", queryset)

class HeadingView(generics.RetrieveUpdateDestroyAPIView):
	queryset = heading.objects.all()
	serializer_class = HeadingSerializer