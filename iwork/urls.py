# -*- coding: utf-8 -*-
#from django.conf.urls import patterns
from django.urls import path
from . import views
#from mysite import views


#urlpatterns = [
#	path('iwork.views',
#	(r'^$','home'),
#	(r'^save_record/$', 'save_record'),
#	(r'^records/$', 'views.records'),
#]

urlpatterns = [
	path(r'^$', iwork.views.home),
	path(r'^save_record/$', iwork.views.save_record),
	path(r'^records/$', iwork.views.records),
]
