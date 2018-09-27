from django.contrib import admin

# Register your models here.
from .models import *

admin.register(Classe)
admin.register(Ordre)
admin.register(Famille)
admin.register(Animal)
