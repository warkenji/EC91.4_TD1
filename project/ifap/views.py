from django.shortcuts import render
from django.views import View

from .models import Classe


class IndexView(View):
    def get(self, request):
        context = {
            'classes': Classe.objects.all()
        }

        return render(request, 'ifap/index.html', context)
