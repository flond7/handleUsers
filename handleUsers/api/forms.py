from django import forms
from django.forms import ModelForm
from .models import customUser
 
 
# creating a form
class customUserForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = customUser
        fields = '__all__'

        labels = {
            'name': '',
            'surname': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'rounded border-none w-100 create-form-input', 'placeholder': 'Nome'}),
            'surname': forms.TextInput(attrs={'class': 'create-form-input', 'placeholder': 'Cognome'})
        }

       # https://www.webforefront.com/django/formtemplatelayout.html