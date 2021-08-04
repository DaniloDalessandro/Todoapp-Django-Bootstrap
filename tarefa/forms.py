from django import forms
from .models import Taregabd
from django.forms import ModelForm

class Conteudoform(forms.ModelForm):
    class Meta:
        model = Taregabd
        fields = ('conteudo',)