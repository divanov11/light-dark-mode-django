from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),

	path('user_settings/', views.userSettings, name="user_settings"),

	path('update_theme/', views.updateTheme, name="update_theme"),

]
