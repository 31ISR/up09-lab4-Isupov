from django import forms 
from . import models
class CreateCommunitie(forms.ModelForm):
    class Meta:
        model = models.Communities
        fields = ['title', 'description', 'slug', 'banner']