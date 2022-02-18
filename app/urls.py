from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='app'),
    path("store", views.index, name='app'),
    path("secondWindow", views.secondWindow, name='app'),
    path("thirdWindow", views.thirdWindow, name='app'),


]