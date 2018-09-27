from django.contrib import admin

# Register your models here.
from .models import Classe, Ordre, Famille, Animal


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ['nom']
    ordering = ['nom']


@admin.register(Ordre)
class OrdreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'classe']
    list_filter = ['classe']
    ordering = ['nom']


@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):
    list_display = ['nom', 'ordre', 'classe']
    list_filter = ['ordre__classe', 'ordre']
    ordering = ['nom']

    def classe(self, obj):
        return obj.ordre.classe


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nom_scientifique', 'nom_commun', 'famille', 'ordre', 'classe']
    list_filter = ['famille__ordre__classe', 'famille__ordre', 'famille']
    ordering = ['nom_scientifique', 'nom_commun']

    def ordre(self, obj):
        return obj.famille.ordre

    def classe(self, obj):
        return obj.famille.ordre.classe

