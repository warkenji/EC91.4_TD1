import csv
from ifap.models import Classe, Ordre, Famille, Animal
from math import floor
from bs4 import BeautifulSoup
import requests
import re
import pandas
import io


page = requests.get("https://www.i-fap.fr/espace-grand-public")

print("Fetching data...")

if page.status_code == 200:
    pattern = re.compile("^https?://www\.i-fap\.fr/uploads/TAXO-i-fap-Grand-Public-V[0-9]+\.xlsx$")

    bsData = BeautifulSoup(page.content, "html.parser")
    for a in bsData.find_all('a', href=True):
        href = a.get('href')
        if pattern.fullmatch(href) is not None:
            try:
                buffer = io.StringIO()
                excelFile = pandas.read_excel(href)
                excelFile.to_csv(buffer, ';', index=False, encoding="utf-8")
                buffer.seek(0)

                print("Merging data...", end='\r')

                Classe.objects.all().delete()

                data = csv.reader(buffer, delimiter=';')
                table = list(enumerate((row for row in data)))
                size = len(table) - 1

                for index, row in table[1:]:

                    classe = Classe.objects.get_or_create(nom=row[0])[0]

                    ordre = Ordre.objects.get_or_create(nom=row[1], classe=classe)[0]

                    famille = Famille.objects.get_or_create(nom=row[2], ordre=ordre)[0]

                    Animal.objects.get_or_create(nom_scientifique=row[3], nom_commun=row[4], famille=famille)

                    print('Merging data... {}%'.format(floor(index / size * 100)), end='\r')

                print("\nData have been pulled with success")
                buffer.close()

            except:
                print("Error on merge data")

else:
    print("Error on fetch data")
