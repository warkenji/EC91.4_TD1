from django.shortcuts import render
from .models import Classe, Ordre, Famille, Animal


def index(request):
    context = {
        'classes': Classe.objects.all()
    }

    return render(request, 'ifap/index.html', context)
