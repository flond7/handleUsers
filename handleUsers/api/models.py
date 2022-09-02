from django.db import models
import uuid
from api.modelsConstants import *

# Create your models here.
class officeMail(models.Model):
  mail = models.CharField(max_length=100, choices = MAIL_OFFICE_CHOICES)
  
  class Meta:
    ordering = []

  def __str__(self):
    return self.title


class customUser(models.Model):
  #_id = models.ObjectIdField()
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  cf = models.CharField(max_length=100, blank=True, default='')

  #MAIL
  hasMail = models.BooleanField()
  personalMail = models.CharField(max_length=100, blank=True, default='')
  officeMail = models.ManyToManyField(officeMail)

  #LAN
  hasLAN = models.BooleanField()
  LANid = models.CharField(max_length=100, blank=True, default='A516-')

  #ADWEB
  hasAdweb = models.BooleanField()
  
  #ASCOT
  hasAscot = models.BooleanField()

  #SDI
  hasSDI = models.BooleanField()

  #ITERATTI
  hasIteratti = models.BooleanField()

  #BOXAPPS
  hasBoxapps = models.BooleanField()

  #WEBSITE
  hasWebsite = models.BooleanField()
  websiteUser = models.BooleanField()
  websiteAdmin = models.BooleanField()

  #ITERATTI
  hasCRM = models.BooleanField()

  #AVCP
  hasAvcp = models.BooleanField()

  #FVG pay
  hasFVGPay = models.BooleanField()

  #SUE
  hasSue = models.BooleanField()

  #SUAP
  #hasSuap = models.BooleanField()

  #SERVIZI SCOLASTICI - Portale Kpax
  hasSercScuola = models.BooleanField()


  class Meta:
    ordering = []

  def __str__(self):
    return self.title


