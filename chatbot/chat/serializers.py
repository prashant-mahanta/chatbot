from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class MessageSerializer(ModelSerializer):

	class Meta:
		model = Messages
		fields = "__all__"