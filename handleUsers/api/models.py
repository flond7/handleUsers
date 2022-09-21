from django.db import models
import uuid
from multiselectfield import MultiSelectField
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

  NOTA
  nei manyToMany fields bisogna mettere obbligatoriamente un valore, per questo quando si creano i vari "uffici" nel db bisogna sempre metterne uno vuoto
  lo standard è inserire un ufficio "--" (così se nella logica bisogna recuperare il fatto che l'ufficio sia vuoto si può fare univocamente)


"""

class officeMail(models.Model):
  mail = models.CharField(max_length = 4, choices = MAIL_OFFICE_CHOICES, default = 'mo0', blank=False)

  def __str__(self):
    return self.mail
""" 
class officeAdweb(models.Model):
  offices = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return self.offices
 """
class officeSDI(models.Model):
  offices = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return self.offices


""" class userEmail (models.Model):
  personalMail = models.CharField("Mail personale", max_length=100, blank=True, default='')
  officeMail = models.ManyToManyField(officeMail)

  def __str__(self):
    return self.personalMail """

class userLan (models.Model):
  lanId = models.CharField("Nome utente rete locale", max_length=100, blank=True, default='A516-')
  lanFolders = models.ManyToManyField(officeMail)

  def __str__(self):
    return self.lanId
""" 
class userAdweb (models.Model):
  adwebId = models.CharField("Nome utente", max_length=100, blank=True, default='A516-')
  adwebOffices = models.ManyToManyField(officeAdweb)

  def __str__(self):
    return self.adwebId
 """
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
  office = models.CharField("Ufficio principale",max_length = 4, choices = MAIN_OFFICE_CHOICES, default = 'b1', blank=False) #assegnazione a un ufficio principale, per capirsi

  #MAIL
  mail = models.CharField("Mail personale", max_length=120, blank=False, default="@comune.aviano.pn.it")
  mailOffice = MultiSelectField(max_length = 100, choices = MAIL_OFFICE_CHOICES, default = 'mo0', blank=False)
  #mailOffices = models.ManyToManyField(officeMail)
  
  #LAN
  #lan = models.ForeignKey(userLan, default=DEFAULT_LAN_ID, on_delete=models.CASCADE)
  lan = models.CharField("ID personale", max_length=120, blank=False, default="A516-")
  lanRole = models.CharField("Ruolo in LAN", max_length = 2, choices = LAN_ROLES_CHOICES, default = 'l1', blank=False)
  lanOffice = MultiSelectField(max_length = 100, choices = LAN_OFFICE_CHOICES, default = 'mo0', blank=False)
  
  #ADWEB
  #adwebOffice = models.CharField(max_length = 4, choices = ADWEB_OFFICES_CHOICES, default = 'ao1', blank=False)
  adwebOffice = MultiSelectField(max_length = 100, choices = ADWEB_OFFICE_CHOICES, default = 'mo0', blank=False)
    
  #ASCOT
  hasAscot = models.BooleanField(default=False)

  #SDI
  hasSDI = models.BooleanField(default=False)
  sdiOffice = MultiSelectField(max_length = 100, choices = ADWEB_OFFICE_CHOICES, default = 's0', blank=False)
  
  #ITERATTI
  hasIteratti = models.BooleanField(default=False)

  #BOXAPPS
  hasBoxapps = models.BooleanField(default=False)
  boxAppsRole = models.CharField(max_length = 4, choices = BOXAPP_ROLES_CHOICES, default = 'b1', blank=False)

  #WEBSITE
  hasWebsite = models.BooleanField(default=False)
  websiteRole = models.CharField(max_length = 2, choices = WEBSITE_ROLES_CHOICES, default = 'w1', blank=False)

  #CRM
  hasCRM = models.BooleanField(default=False)
  crmRole = models.CharField(max_length = 2, choices = CRM_ROLES_CHOICES, default = 'c1', blank=False)

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

  #ALBO PRETORIO
  hasAlboPret = models.BooleanField(default=False)

  note = models.TextField(default="")

  #DISATTIVAZIONI
  mailDeleted = models.BooleanField("Mail disattivata", default=False)
  lanDeleted = models.BooleanField("Lan disattivata", default=False)
  adwebDeleted = models.BooleanField("Adweb disattivato", default=False)
  ascotDeleted = models.BooleanField("Ascot disattivato", default=False)
  sdiDeleted = models.BooleanField("SDI disattivato", default=False)
  iterattiDeleted = models.BooleanField("SDI disattivato", default=False)
  boxAppsDeleted = models.BooleanField("SDI disattivato", default=False)
  websiteDeleted = models.BooleanField("Sito disattivato", default=False)
  crmDeleted = models.BooleanField("CRM disattivato", default=False)
  avcpDeleted = models.BooleanField("AVCP disattivato", default=False)
  servScuolaDeleted = models.BooleanField("Servizi scolastici disattivato", default=False)
  alboPretDeleted = models.BooleanField("Albo pretorio disattivato", default=False)

  class Meta:
    ordering = []

  def __str__(self):
    return self.name


