import mailbox
from django.db import models
import uuid
from api.modelsConstants import *

# Create your models here.

# Default ids are needed because it is impossible to add a non-nullable field 'adweb' to customuser without specifying a default.
DEFAULT_MAIL_ID = 1
DEFAULT_ADWEB_ID = 1
DEFAULT_LAN_ID = 1

""" 
- per ogni applicativo ho degli uffici che sono classi officeXXXXXXX
  (es: officeMail sono le mail uffici, officeAdweb sono gli uffici in adweb...)
  questo sarà l'elenco a scelta multipla che potrò visualizzare per gli utenti
- registrare le classi officeXXX nel file admin.py in modo da farle visualizzare nel backend
- ogni utente ha una classe userXXXXX (es: userMail, userAsweb)
  che raccoglie tutte le informazioni dell'utente relative a quell'applicazione
  --- per visualizzare l'elenco a scelta multipla bisogna usare model.ManyToManyFiels(officeXXX)

"""

class officeMail(models.Model):
  mail = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return self.mail

class officeAdweb(models.Model):
  offices = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return self.offices

class officeSDI(models.Model):
  offices = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return self.offices


class userEmail (models.Model):
  personalMail = models.CharField("Mail personale", max_length=100, blank=True, default='')
  officeMail = models.ManyToManyField(officeMail)

  def __str__(self):
    return self.personalMail

class userLan (models.Model):
  lanId = models.CharField("Nome utente rete locale", max_length=100, blank=True, default='A516-')
  lanFolders = models.ManyToManyField(officeMail)

  def __str__(self):
    return self.lanId

class userAdweb (models.Model):
  adwebId = models.CharField("Nome utente", max_length=100, blank=True, default='A516-')
  adwebOffices = models.ManyToManyField(officeAdweb)

  def __str__(self):
    return self.adwebId

class userSDI (models.Model):
  sdiId = models.CharField("LOGIN FVG", max_length=100, blank=True, default='')
  sdiOffices = models.ManyToManyField(officeSDI)

  def __str__(self):
    return self.sdiId


class customUser(models.Model):
  #_id = models.ObjectIdField()
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField("Nome", max_length=100, blank=True, default='')
  surname = models.CharField("Cognome", max_length=100, blank=True, default='')
  cf = models.CharField("Codice fiscale", max_length=100, blank=True, default='')

  #MAIL
  mail = models.CharField("Mail personale", max_length=120, blank=False, default="@comune.aviano.pn.it")
  mailOffices = models.ManyToManyField(officeMail)
  mailDeleted = models.BooleanField("Mail - Cancellata / disattivata", default=False)

  #LAN
  #lan = models.ForeignKey(userLan, default=DEFAULT_LAN_ID, on_delete=models.CASCADE)
  lan = models.CharField("ID personale", max_length=120, blank=False, default="A516-")
  lanDeleted = models.BooleanField("Lan - Cancellata / disattivata", default=False)

  #ADWEB
  adweb = models.ForeignKey(userAdweb, default=DEFAULT_ADWEB_ID, on_delete=models.CASCADE)
  adwebOffices = models.ManyToManyField(officeAdweb)
  adwebDeleted = models.BooleanField("Adweb - Cancellato / disattivato", default=False)
  
  #ASCOT
  hasAscot = models.BooleanField(default=False)

  #SDI
  hasSDI = models.BooleanField(default=False)
  sdiOffices = models.ManyToManyField(officeSDI)
  sdiDeleted = models.BooleanField("SDI - Cancellato / disattivato", default=False)

  #ITERATTI
  hasIteratti = models.BooleanField(default=False)

  #BOXAPPS
  hasBoxapps = models.BooleanField(default=False)

  #WEBSITE
  hasWebsite = models.BooleanField(default=False)
  websiteUser = models.BooleanField(default=False)
  websiteAdmin = models.BooleanField(default=False)

  #ITERATTI
  hasCRM = models.BooleanField(default=False)
  crmDeleted = models.BooleanField("CRM - Cancellato / disattivato", default=False)

  #AVCP
  hasAvcp = models.BooleanField(default=False)

  #FVG pay
  hasFVGPay = models.BooleanField(default=False)

  #SUE
  hasSue = models.BooleanField(default=False)

  #SUAP
  #hasSuap = models.BooleanField()

  #SERVIZI SCOLASTICI - Portale Kpax
  hasServScuola = models.BooleanField(default=False)
  servScuolaDeleted = models.BooleanField("Servizi scolastici - Cancellato / disattivato", default=False)

  #ALBO PRETORIO
  hasAlboPret = models.BooleanField(default=False)
  alboPretDeleted = models.BooleanField("Albo pretorio - Cancellato / disattivato", default=False)

  note = models.TextField(default="")

  class Meta:
    ordering = []

  def __str__(self):
    return self.name

