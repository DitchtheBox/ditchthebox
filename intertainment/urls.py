from django.conf.urls import patterns, url, include
from intertainment import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),	
)
