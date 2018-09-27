from django.db import models

# Create your models here.


class Classe(models.Model):
    nom = models.CharField(max_length=255)


class Ordre(models.Model):
    nom = models.CharField(max_length=255)
    classe = models.ForeignKey(Classe, models.CASCADE)


class Famille(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.ForeignKey(Ordre, models.CASCADE)


class Animal(models.Model):
    nom_commun = models.CharField(max_length=255)
    nom_scientifique = models.CharField(max_length=255)
    famille = models.ForeignKey(Famille, models.CASCADE)
