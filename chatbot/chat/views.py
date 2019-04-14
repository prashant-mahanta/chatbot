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
			if file == None:
				pass
			else:
				instance = Messages(file=file,user=user)
				
		elif text != None:
			if file == None:
				instance = Messages(text=text,file=None,user=user)
			else:
				instance = Messages(text=text, file=file, user=user)
		if text == None and file == None:
			pass
		else:
			print("instance file",instance.file)
			if instance.file == None:
				print("Hurray")
			else:
				print(instance.file)
			print("instance text",instance.text)
			instance.save()
		print("save hogaya",text, file)
		serialized_object = MessageSerializer(instance, many=False)
		return Response(serialized_object.data)
	
	def put(self, request, format=None):
		if request.data.get("feedback-or-file") == "1":
			score = request.data.get("bot-feedback")
			messages = Messages.objects.all()[::-1]

			for message in messages:
				if message.user == 1:
					print(message.text, message.id)
					mid = message.id
					break
			instance = Messages.objects.get(id=mid)
			print(instance.text,mid)
			instance.text = instance.text
			instance.file = instance.file
			instance.bot_feedback = int(score)
			instance.save()
			serialized_object = MessageSerializer(instance, many=False)
			return Response(serialized_object.data)

		else:
			messages = Messages.objects.all()
			files = []
			for i in messages:
				if i.file.name:
					files.append(i)
			serialized_object = MessageSerializer(files, many=False)
			print(serialized_object)
			return Response(serialized_object.data)
		

def main(request):
	messages = Messages.objects.all()
	# print(messages)
	context={"messages": messages}
	files = []
	for i in messages:
		if i.file.name:
			files.append(i)
	context["files"]=files
	return render(request, 'index.html', context)