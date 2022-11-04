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
  #id = models.AutoField(primary_key=True)
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField("Nome", max_length=100, blank=True, default='')
  surname = models.CharField("Cognome", max_length=100, blank=True, default='')
  cf = models.CharField("Codice fiscale", max_length=100, blank=True, default='')
  office = models.CharField("Ufficio principale",max_length = 4, choices = MAIN_OFFICE_CHOICES, default = 'o0', blank=False) #assegnazione a un ufficio principale, per capirsi

  #MAIL
  mail = models.CharField("Mail personale", max_length=120, blank=False, default="@comune.aviano.pn.it")
  mailOffice = MultiSelectField(max_length = 100, choices = MAIL_OFFICE_CHOICES, default = 'mo0', blank=False)
  
  #LAN
  #lan = models.ForeignKey(userLan, default=DEFAULT_LAN_ID, on_delete=models.CASCADE)
  lan = models.CharField("ID personale", max_length=120, blank=False, default="A516-")
  lanRole = models.CharField("Ruolo in LAN", max_length = 2, choices = LAN_ROLES_CHOICES, default = 'l1', blank=False)
  lanOffice = MultiSelectField(max_length = 100, choices = LAN_OFFICE_CHOICES, default = 'mo0', blank=False)
  lanNote = models.CharField("Note per lan", max_length = 150, default='', blank=True)
  
  #ADWEB
  adwebOffice = MultiSelectField(max_length = 100, choices = ADWEB_OFFICE_CHOICES, default = 'mo0', blank=False)
  adwebRole = models.CharField("Ruolo in adweb", max_length = 4, choices = ADWEB_ROLES_CHOICES, default = 'a0', blank=False)
  adwebNote = models.CharField("Note per adweb", max_length = 150, default='', blank=True)
    
  #ASCOT
  ascotRole = models.CharField("Ruolo Ascot", max_length = 4, choices = ASCOT_ROLES_CHOICES, default = 'a0', blank=False)
  ascotOffice = MultiSelectField("Uffici Ascot", max_length = 100, choices = ASCOT_OFFICE_CHOICES, default = 'a0', blank=False)

  #SDI
  sdiRole = models.CharField("Ruolo in SDI", max_length = 4, choices = SDI_ROLES_CHOICES, default = 'sdi0', blank=False)
  sdiOffice = MultiSelectField("Uffici SDI", max_length = 100, choices = SDI_OFFICE_CHOICES, default = 'sdi0', blank=False)
  
  #GIFRA - ITERATTI
  iteratti = models.CharField("ID iteratti", max_length=120, blank=True, default="")
  iterattiRole = models.CharField(max_length = 2, choices = ITERATTI_ROLES_CHOICES, default = 'i0', blank=False)
  iterattiOffice = MultiSelectField("Uffici iteratti", max_length = 100, choices = ITERATTI_OFFICE_CHOICES, default = 'i0', blank=False)

  #BOXAPPS
  boxAppsRole = models.CharField(max_length = 4, choices = BOXAPP_ROLES_CHOICES, default = 'b1', blank=False)

  #MASTERDATA
  masterDataRole = models.CharField(max_length = 4, choices = MASTERDATA_ROLES_CHOICES, default = 'm1', blank=False)

  #WEBSITE
  websiteRole = models.CharField(max_length = 2, choices = WEBSITE_ROLES_CHOICES, default = 'w0', blank=False)

  #CRM
  crmRole = models.CharField(max_length = 2, choices = CRM_ROLES_CHOICES, default = 'c0', blank=False)

  #AVCP
  avcpRole = models.CharField(max_length = 2, choices = AVCP_ROLES_CHOICES, default = 'a0', blank=False)

  #FVG pay
  fvgPayRole = models.CharField(max_length = 2, choices = FVGPAY_ROLES_CHOICES, default = 's0', blank=False)

  #SUE
  sueRole = models.CharField(max_length = 2, choices = SUE_ROLES_CHOICES, default = 's0', blank=False)

  #SUAP
  suapRole = models.CharField(max_length = 2, choices = SUAP_ROLES_CHOICES, default = 's0', blank=False)

  #SERVIZI SCOLASTICI - Portale Kpax
  servScolRole = models.CharField(max_length = 4, choices = SERVSCOL_ROLES_CHOICES, default = 'ss0', blank=False)

  #ALBO PRETORIO
  alboPretRole = models.CharField(max_length = 4, choices = ALBOPRET_ROLES_CHOICES, default = 'ap0', blank=False)

  note = models.TextField(default="", blank=True)
  active = models.BooleanField(default=True)

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
  masterdataDeleted = models.BooleanField("Masterdata eliminato", default=False)

  class Meta:
    ordering = []

  def __str__(self):
    return self.name + ' ' + self.surname


