from django.contrib import admin

# Register your models here.
from .models import customUser, askUser, officeMail, officeSDI, userLan #, officeAdweb, userAdweb,userEmail,

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.
# it allows to have a user friendly interface to input data in the db

#admin.site.register(User)
admin.site.register(customUser)
admin.site.register(askUser)

