import csv
from ifap.models import *

with open('data/data.csv', newline='') as fichier:
    data = csv.reader(fichier, delimiter=';')
    table = list(enumerate((row for row in data)))
    size = len(table) - 1

    print("Update data started ")

    for index, row in table:
        if index > 0:
            classe = Classe.objects.get_or_create(nom=row[0])[0]

            ordre = Ordre.objects.get_or_create(nom=row[1], classe=classe)[0]

            famille = Famille.objects.get_or_create(nom=row[2], ordre=ordre)[0]

            Animal.objects.get_or_create(nom_scientifique=row[3], nom_commun=row[4], famille=famille)

            print('\rAnimal update: %d / %d' % (index, size), end='')

    print("\nData updated")
