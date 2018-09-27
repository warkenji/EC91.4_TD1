from django.db import models

# Create your models here.


class Classe(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Ordre(models.Model):
    nom = models.CharField(max_length=255)
    classe = models.ForeignKey(Classe, models.CASCADE)

    def __str__(self):
        return self.nom


class Famille(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.ForeignKey(Ordre, models.CASCADE)

    def __str__(self):
        return self.nom


class Animal(models.Model):
    nom_commun = models.CharField(max_length=255)
    nom_scientifique = models.CharField(max_length=255)
    famille = models.ForeignKey(Famille, models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.nom_commun, self.nom_scientifique)
