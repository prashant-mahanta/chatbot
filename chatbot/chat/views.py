from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *

class ChatAppView(APIView):
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		objects = Messages.objects.all()
		serialized_object = MessageSerializer(objects,many=True)
		return Response(serialized_object.data)

	def post(self, request, format=None):
		text = request.data.get("text")
		user = request.data.get("user")
		if user == None:
			user = 0
		else:
			user = int(user)

		file = None
		if request.FILES.get('file-q'):
			file = request.FILES.getlist('file-q')[0]
		if text == None:
			instance = Messages(file=file,user=user)
		if file == None:
			instance = Messages(text=text,user=user)

		if text == None and file == None:
			pass
		else:
			instance.save()
		print("save hogaya",text, file)
		serialized_object = MessageSerializer(instance,many=False)
		return Response(serialized_object.data)


def main(request):
	messages = Messages.objects.all()
	# print(messages)
	context={"messages": messages}
	return render(request, 'index.html', context)