from django.shortcuts import render,redirect
from .models import Taregabd
from .forms import Conteudoform

# Create your views here.

def index(request):
    conteudo = Taregabd.objects.all()
    form = Conteudoform()
    if request.method == 'POST':
        form = Conteudoform(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/')
    context = {
        'conteudos':conteudo,
        'form':form

    }

    return render(request,'lista.html',context)


def delete_tarefa(request,id):
    deleteTarefa = Taregabd.objects.get(id=id)
    deleteTarefa.delete()
    return redirect('/')

