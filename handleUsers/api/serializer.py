from rest_framework import serializers
from .models import customUser

from api.modelsConstants import PATH_STATUS_CHOICES, CITIZENSHIP_CHOICES

class customUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = customUser
    fields = '__all__'
    depth = 1