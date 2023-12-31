import subprocess
import os
from Klasse.CreateAndEditRowGewerkteUren import edit_row_gewerkte_uren, add_to_gewerkte_uren
from Klasse.CreateAndEditRowOmzet import edit_row_omzet, add_to_omzet
import Klasse.CreateDB as create_database
import Klasse.CreateCSV as CreatCSV
import Klasse.CreateExcel as CreateExcel

def create_database():
     script_path = os.path.join('Klasse', 'CreateDB.py')
     try:
        subprocess.run(['python', script_path], check=True)
        print("Database aangemaakt.")
     except subprocess.CalledProcessError as e:
        print(f"Fout bij het uitvoeren van het script: {e}")

create_database()
#Uw database zou moeten aangemaakt zijn. (Indien niet -> zie path in klasse:CreateDB of .gitignore)

# Voorbeeld van het toevoegen van een nieuwe rij aan de tabel 'omzet'
# Vervang deze waarden door de werkelijke waarden die je wilt toevoegen
# Gebruikte format = YYYY/MM/DD
add_to_omzet('2020-01-12' , 500)
edit_row_omzet(1,'2022-01-12' , 1000)
add_to_gewerkte_uren('2020-01-22',5)
edit_row_gewerkte_uren(1,'2020-01-22',3)


