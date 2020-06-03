from rest_framework import serializers

from .models import *

class UserSerailizer(serializers.ModelSerializer):
	class Meta:
		model = Setting
		fields = '__all__'
