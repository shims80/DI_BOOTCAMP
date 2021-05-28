from .models import *
from django import forms


class CategoryForm(forms.Form):
    name =forms.CharField(max_length=100) 

class GifForm(forms.Form):
    uploader_name= forms.CharField(max_length=100)
    title =forms.CharField(max_length=100) 
    url=forms.URLField(max_length=200) 
    categories =forms.ModelMultipleChoiceField(queryset=Category.objects.all()) 

