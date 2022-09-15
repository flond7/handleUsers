from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .models import customUser

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/woman-list/',
    'Detail':'/woman-detail/<str:pk>',
    'Create':'/woman-create/',
    'Update':'/woman-update/<str:pk>',
    'Delete':'/woman-delete/<str:pk>',
  }
  return Response(basicApi_urls)

""" @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    return render(request, 'templates/login.html') """

#@login_required(login_url="/login/")
def user_overview(request):
    userList = customUser.objects.all()
    return render(request, 'user_overview.html', {'userList': userList})

