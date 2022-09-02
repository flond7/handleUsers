from django.db import models
import uuid
from api.modelsConstants import *

# Create your models here.
class officeMail(models.Model):
  #mail = models.CharField(max_length=100, choices = MAIL_OFFICE_CHOICES)
  mail = models.CharField(max_length=100, blank=True, default='')
  
  class Meta:
    ordering = []

  def __str__(self):
    return self.mail


class customUser(models.Model):
  #_id = models.ObjectIdField()
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField("Nome", max_length=100, blank=True, default='')
  surname = models.CharField("Cognome", max_length=100, blank=True, default='')
  cf = models.CharField("Codice fiscale", max_length=100, blank=True, default='')

  #MAIL
  hasMail = models.BooleanField("Ha una mail")
  personalMail = models.CharField("Mail personale", max_length=100, blank=True, default='')
  officeMail = models.ManyToManyField(officeMail)

  #LAN
  hasLAN = models.BooleanField()
  LANid = models.CharField("Nome utente rete locale", max_length=100, blank=True, default='A516-')

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
    return self.name


