"""
Author :    Marc Taron
Version :   1.0
Name :      AppOne/urls.py
Date :      XX/XX/XX

Docstring : This file define the urls pattern for the AppOne
"""

# Import path, views...
from django.urls import path
from . import views

# Definition of AppName used for namespace
app_name = 'AppOne'

# Definition of the urls patterns for the current App
urlpatterns = [
    path('', views.defaultview, name='defaultview'),
]
