from django import forms
from .models import customUser
 
 
# creating a form
class customUserForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = customUser
 
        # specify fields to be used
        fields = '__all__'