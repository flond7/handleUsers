from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .constants import MY_CONST
from .modelsConstants import *
from .models import customUser
from .serializer import customUserSerializer
from .forms import customUserForm
from .filters import customUserFilter

#@login_required
#@permission_required('polls.add_choice', raise_exception=True)
def user_overview(request):
    userList = customUser.objects.all().order_by('name')
    # if the dictionary has some values the boolean is true, otherwise false
    if bool(request.GET):
      user_filter = customUserFilter(request.GET, queryset=userList)
      # get params from url
      name = request.GET.get('name')
      surname = request.GET.get('surname')
      office = request.GET.get('office')
      active = request.GET.get('active')
      # if the search is for active/inactive users check user params
      if active == 'True':
        print('active')
      elif active == 'False':
        print('inactive')
      
      # ATTENTION: django-filters puts the result inside a qs so you have to pass user_filter.qs
      return render(request, 'user_overview.html', {'userList': user_filter.qs, 'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 'url_office':office, 'surname':surname,'name':name })
    else:
      return render(request, 'user_overview.html', {'userList': userList, 'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES}) 

#@login_required
#@permission_required('customuser.add_choice', raise_exception=True)
def user_create(request):
    u = customUser()
    submitted = False
    if request.method == "POST":
      
        print(request.POST.getlist('lanOffice'))
        print(request.POST.get('lanOffice'))
        print(request.POST.getlist('ascotOffice'))
        cu = customUserForm(request.POST)
        #print(cu)
        print(u.ascotOffice)
        if cu.is_valid():
            cu.save()
            return HttpResponseRedirect('user_create?submitted=True')
        else:
            render(request, 'user_create.html', {'form': cu, 'submitted': submitted, 'MY_CONST': MY_CONST, 
    'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
    'LAN_OFFICE_CHOICES':LAN_OFFICE_CHOICES, 'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES, 
    'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 
    'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':SDI_OFFICE_CHOICES,
    'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':ITERATTI_OFFICE_CHOICES,
    'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':ASCOT_OFFICE_CHOICES,
    'ASCOT_OFFICE_CHOICES':ASCOT_OFFICE_CHOICES, 'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES,
    'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
    'SERVSCOL_ROLES_CHOICES':SERVSCOL_ROLES_CHOICES, 'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
    'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
    'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
    'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES})
        # if user is new then set active to true
        # if the user is modified check if it's still active 


    else:
        cu = customUserForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'user_create.html', {'form': cu, 'submitted': submitted, 'MY_CONST': MY_CONST, 
    'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
    'LAN_OFFICE_CHOICES':LAN_OFFICE_CHOICES, 'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES, 
    'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 
    'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':SDI_OFFICE_CHOICES,
    'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':ITERATTI_OFFICE_CHOICES,
    'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':ASCOT_OFFICE_CHOICES,
    'ASCOT_OFFICE_CHOICES':ASCOT_OFFICE_CHOICES, 'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES,
    'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
    'SERVSCOL_ROLES_CHOICES':SERVSCOL_ROLES_CHOICES, 'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
    'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
    'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
    'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES})

#@login_required
#@permission_required('customuser.add_choice', raise_exception=True)
def user_edit(request, pk):
    u = customUser.objects.get(id=pk)
    
    print(u.adwebOffice)
    print(u.lanOffice)

    # MAIL iterate the office to check the selected ones
    checked_mail_offices = list(MAIL_OFFICE_CHOICES)
    for i in range(len(MAIL_OFFICE_CHOICES)):
      checked_mail_offices[i] = list(checked_mail_offices[i])
      if MAIL_OFFICE_CHOICES[i][0] in u.mailOffice:
        checked_mail_offices[i].append('checked')
      else:
        checked_mail_offices[i].append('unchecked')
    
    # LAN iterate the office to check the selected ones
    checked_lan_offices = list(LAN_OFFICE_CHOICES)
    for i in range(len(LAN_OFFICE_CHOICES)):
      checked_lan_offices[i] = list(checked_lan_offices[i])
      if LAN_OFFICE_CHOICES[i][0] in u.lanOffice:
        checked_lan_offices[i].append('checked')
      else:
        checked_lan_offices[i].append('unchecked')

    # ADWEB iterate the office to check the selected ones
    checked_adweb_offices = list(ADWEB_OFFICE_CHOICES)
    for i in range(len(ADWEB_OFFICE_CHOICES)):
      checked_adweb_offices[i] = list(checked_adweb_offices[i])
      if ADWEB_OFFICE_CHOICES[i][0] in u.adwebOffice:
        checked_adweb_offices[i].append('checked')
      else:
        checked_adweb_offices[i].append('unchecked')

    # ASCOT iterate the office to check the selected ones
    checked_ascot_offices = list(ASCOT_OFFICE_CHOICES)
    for i in range(len(ASCOT_OFFICE_CHOICES)):
      checked_ascot_offices[i] = list(checked_ascot_offices[i])
      if ASCOT_OFFICE_CHOICES[i][0] in u.ascotOffice:
        checked_ascot_offices[i].append('checked')
      else:
        checked_ascot_offices[i].append('unchecked')

    # SDI iterate the office to check the selected ones
    checked_sdi_offices = list(SDI_OFFICE_CHOICES)
    for i in range(len(SDI_OFFICE_CHOICES)):
      checked_sdi_offices[i] = list(checked_sdi_offices[i])
      if SDI_OFFICE_CHOICES[i][0] in u.sdiOffice:
        checked_sdi_offices[i].append('checked')
      else:
        checked_sdi_offices[i].append('unchecked')

    # ITERATTI iterate the office to check the selected ones
    checked_iteratti_offices = list(ITERATTI_OFFICE_CHOICES)
    for i in range(len(ITERATTI_OFFICE_CHOICES)):
      checked_iteratti_offices[i] = list(checked_iteratti_offices[i])
      if ITERATTI_OFFICE_CHOICES[i][0] in u.iterattiOffice:
        checked_iteratti_offices[i].append('checked')
      else:
        checked_iteratti_offices[i].append('unchecked')

    if request.method == "POST":
        u.save()
        cu = customUserForm(request.POST)
        
        print(cu.get)
        print(u)
        if cu.is_valid():
            cu.save()
            print("VALID")
            #return HttpResponseRedirect('profile.html')
        else:
            print("PRINT")
    else:
        cu = customUserForm()
    return render(request, 'user_create.html', {'u':u, 'MY_CONST': MY_CONST, 
    'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
    'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES,'LAN_OFFICE_CHOICES':checked_lan_offices, 
    'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': checked_adweb_offices, 
    'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':checked_sdi_offices,
    'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':checked_iteratti_offices,
    'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':checked_ascot_offices,
    'MAIL_OFFICE_CHOICES': checked_mail_offices,
    'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
    'SERVSCOL_ROLES_CHOICES': SERVSCOL_ROLES_CHOICES, 'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
    'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
    'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
    'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES})

def user_update(request):
  cu = customUserForm()
  if request.method == "POST":
    cu = customUserForm(request.POST) 
    if cu.is_valid():
      cu.save()
      return HttpResponseRedirect('user_overview')
    else:
      return HttpResponse("your form is wrong")

def user_add(request):
  cu = customUserForm()
  if request.method == "POST":
    cu = customUserForm(request.POST) 
    if cu.is_valid():
      cu.save()
      return HttpResponseRedirect('user_overview')
    else:
      return HttpResponse("your form is wrong")

def index(request):
    userList = customUser.objects.all()
    return render(request, 'index.html', {'userList': userList, 'MY_CONST': MY_CONST})

def info(request):
    return render(request, 'account_info.html', {'MY_CONST': MY_CONST})

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