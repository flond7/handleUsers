from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .constants import MY_CONST
from .modelsConstants import *
from .models import customUser
from .serializer import customUserSerializer
from .forms import customUserForm
from .filters import customUserFilter

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

#@login_required
#@permission_required('polls.add_choice', raise_exception=True)
def user_overview(request):
    userList = customUser.objects.all().order_by('name')
    #if the dictionary has some values the boolean is true, otherwise false
    if bool(request.GET):
      user_filter = customUserFilter(request.GET, queryset=userList)
      #get params from url
      name = request.GET.get('name')
      surname = request.GET.get('surname')
      office = request.GET.get('office')
      print(user_filter.qs)
      # ATTENTION: django-filters puts the result inside a qs so you have to pass user_filter.qs
      return render(request, 'user_overview.html', {'userList': user_filter.qs, 'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 'url_office':office, 'surname':surname,'name':name })
    else:
      return render(request, 'user_overview.html', {'userList': userList, 'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES}) 

@login_required
@permission_required('customuser.add_choice', raise_exception=True)
def user_create(request):
    return render(request, 'user_create.html', {'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 'LAN_OFFICE_CHOICES':LAN_OFFICE_CHOICES, 'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES, 'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES})

def user_add(request):
  cu = customUserForm()
  if request.method == "POST":
    cu = customUserForm(request.POST)
    if cu.is_valid():
      cu.save()
      return HttpResponseRedirect('user_overview')
    else:
      return HttpResponse("your form is wrong")
    

    """ if form.is_valid():
      cu = form.save(commit=False)
      print("OK")
    else:
      print("ERR") """

def index(request):
    userList = customUser.objects.all()
    return render(request, 'index.html', {'userList': userList, 'MY_CONST': MY_CONST})

@api_view(['GET'])
def profile(request, pk):
  u = customUser.objects.get(id=pk)
  MY_MODEL_CONST = {'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES}
  return render(request, 'profile.html', {'u': u, 'MY_CONST': MY_CONST, 'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES })

@api_view(['GET'])
def adweb(request):
  u = customUser.objects.all()
  #u_filter = customUserFilter(request.GET, queryset=u)
  MY_MODEL_CONST = {'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES}
  #return render(request, 'adweb.html', {'userList': u, 'MY_CONST': MY_CONST, 'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'filter': u_filter })
  return render(request, 'adweb.html', {'userList': u, 'MY_CONST': MY_CONST, 'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES })