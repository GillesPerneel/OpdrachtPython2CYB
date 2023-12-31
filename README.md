# OpdrachtPython2CYB

In deze opdracht gaan we tewerk in een winkel.
Hier hebben we 2 database tabellen die we gaan kunnen veranderen + dingen toevoegen.
Deze tabellen zijn: gewerkte uren + omzet gegenereerd in de gewerkte uren
Wat is het doel hiervan? 
Zo kunnen we na gaan hoeveel er gemiddeld wordt verkocht in bepaalde uren vb. na een uur .



Functionaliteiten:
    edit_row_gewerkte_uren          vb.edit_row_gewerkte_uren(1,'2020-01-22',3)
    add_to_gewerkte_uren            vb.add_to_gewerkte_uren('2020-01-22',5)
    edit_row_omzet                  vb.edit_row_omzet(1,'2022-01-12' , 1000)
    add_to_omzet                    vb.add_to_omzet('2020-01-12' , 500)

Bestanden verkrijgen:
    CSV: 
       Data = get_omzet_data() -> Data omzetten in bruikbare data voor CSV file
       export_to_csv(Data, 'OmzetData_31_12.csv') -> Data exporteren naar CSV file
    Excel:
        DataEx = get_omzet_dataExcel() -> Data omzetten in bruikbare data voor Excel File
        export_to_excel(DataEx , 'OmzetData_31_12.xlsx') -> Excel File aanmaken en exporteren