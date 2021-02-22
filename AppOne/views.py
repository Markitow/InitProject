"""
Author :    Marc Taron
Version :   1.0
Name :      AppOne/views.py
Date :      XX/XX/XX

Docstring : This file define the differents views of the AppOne
"""

# Definition of Import packages

# Default
from django.shortcuts import render

# Import json
import json

# Import models you defined in the models file
from AppOne import models

# Import forms you defined in the forms file
# from .forms import FormName

# Import some differents responses used to debug
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Import to serialize before save object
from django.core import serializers

# Import standard User Django environment
from django.contrib.auth.models import User

# Import tools to redirect if user not logged
from django.contrib.auth.decorators import login_required

# Import date dealers
from datetime import datetime, date

# Import tools to show information/alert messages
from django.contrib import messages

# Import tools to paginate result
from django.core.paginator import Paginator

# Import tools to aggregate and add informations to datas from database
from django.db.models import Avg, Count, Q, Max, F, OuterRef, Subquery

# Create your views here.


# Default view
# If you want the user to be logged :
# @login_required(login_url='AppName:FunctionName')
def defaultview(request):

    # Do something

    # Context to pass variables to template and javascript
    context = {
        'VarOne': 'ValueOne',
    }

    # Return for debug
    # return HttpResponse('TextOrVariableForDebug')
    # Return a template view
    return render(request, 'AppOne/defaulttemplate.html', context)
