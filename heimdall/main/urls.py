from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
	# url(r'^', views.api_root,),
	url(r'^traffic/$', views.TrafficView.as_view(), name='traffic-list',),
	url(r'^traffic/(?P<pk>[0-9]+)/$', views.TrafficDetailView.as_view(), name='traffic-detail'),
	url(r'^location/$', views.LocationView.as_view(), name='location-list'),
	# whenever you want to edit, you'll edit here
	url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail'),
	url(r'^front/', views.SendValue,)
])


urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 