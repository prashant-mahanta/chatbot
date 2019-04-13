from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import url


namespace = 'chat'
urlpatterns = [
	path('', main, name="main"),

	# api to post and retrive chats user message
	path('api-message/', ChatAppView.as_view(), name="ChatAppView"),
]