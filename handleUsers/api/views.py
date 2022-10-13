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
#from api.filters import customUserFilter

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
    userList = customUser.objects.all()
    return render(request, 'user_overview.html', {'userList': userList, 'MY_CONST': MY_CONST})

@login_required
@permission_required('customuser.add_choice', raise_exception=True)
def user_create(request):
    return render(request, 'user_create.html', {'MY_CONST': MY_CONST, 'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES})

def user_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def index(request):
    userList = customUser.objects.all()
    return render(request, 'index.html', {'userList': userList, 'MY_CONST': MY_CONST})

""" def profile(request,):
    userList = customUser.objects.all()
    return render(request, 'profile.html', {'userList': userList, 'MY_CONST': MY_CONST}) """

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