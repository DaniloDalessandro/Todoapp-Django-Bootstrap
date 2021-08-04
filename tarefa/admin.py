from django.contrib import admin
from .models import Taregabd

# Register your models here.

@admin.register(Taregabd)

class Tarefaadm(admin.ModelAdmin):
    list_display = ['id','conteudo','data']

