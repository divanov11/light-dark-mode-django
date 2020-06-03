from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Setting(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

	def __str__(self):
		return self.name