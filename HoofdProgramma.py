import subprocess
import os
import openpyxl 
import xlsxwriter
from Klasse.CreateAndEditRowGewerkteUren import edit_row_gewerkte_uren, add_to_gewerkte_uren
from Klasse.CreateAndEditRowOmzet import edit_row_omzet, add_to_omzet
import Klasse.CreateDB as create_database
from Klasse.CreateExcelFile import get_omzet_dataExcel , export_to_excel
from Klasse.CreateCSVFile import get_omzet_data, export_to_csv

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



Data = get_omzet_data()
export_to_csv(Data, 'OmzetData_31_12.csv')
DataEx = get_omzet_dataExcel()
export_to_excel(DataEx , 'OmzetData_31_12.xlsx')


