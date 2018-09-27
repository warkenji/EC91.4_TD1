import csv
from ifap.models import Classe, Ordre, Famille, Animal
from math import floor

print("Pulling data...", end='\r')

Classe.objects.all().delete()

with open('data/data.csv', newline='') as fichier:
    data = csv.reader(fichier, delimiter=';')
    table = list(enumerate((row for row in data), -1))
    size = len(table) - 1

    for index, row in table[1:]:
        print('Pulling data... {}%'.format(floor(index / size * 100)), end='\r')

        classe = Classe.objects.get_or_create(nom=row[0])[0]

        ordre = Ordre.objects.get_or_create(nom=row[1], classe=classe)[0]

        famille = Famille.objects.get_or_create(nom=row[2], ordre=ordre)[0]

        Animal.objects.get_or_create(nom_scientifique=row[3], nom_commun=row[4], famille=famille)

    print("Data have been pulled with success")

    fichier.close()
