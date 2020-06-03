from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

from .serializers import UserSerailizer

# Create your views here.

def index(request):
	return render(request, 'base/index.html')

def userSettings(request):
	user, created = User.objects.get_or_create(id=1)
	setting = user.setting

	seralizer = UserSerailizer(setting, many=False)

	return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
	data = json.loads(request.body)
	theme = data['theme']
	
	user, created = User.objects.get_or_create(id=1)
	user.setting.value = theme
	user.setting.save()
	print('Request:', theme)
	return JsonResponse('Updated..', safe=False)