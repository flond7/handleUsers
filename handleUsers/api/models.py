from django.db import models

# Create your models here.
class author(models.Model):
  _id = models.ObjectIdField()
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  cf = models.CharField(max_length=100, blank=True, default='')

  #MAIL
  hasMail = models.BooleanField()
  personalMail = models.CharField(max_length=100, blank=True, default='')
  officeMail = models.CharField(max_length=100, blank=True, default='')

  #LAN

  #ADWEB

  #ASCOT

  #SDI

  #WEBSITE
  hasWebsite = models.BooleanField()




  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.title