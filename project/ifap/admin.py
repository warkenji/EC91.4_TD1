from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Classe)
admin.site.register(Ordre)
admin.site.register(Famille)
admin.site.register(Animal)
