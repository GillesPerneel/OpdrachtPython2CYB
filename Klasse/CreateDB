import os
import sqlite3

if not os.path.exists('DB'):
    os.makedirs('DB')

conn = sqlite3.connect('DB/vb_database.db')

cursor = conn.cursor()
create_omzet_table = '''
CREATE TABLE IF NOT EXISTS omzet (
    id INTEGER PRIMARY KEY,
    datum TEXT,
    bedrag INTEGER
);
'''
create_gewerkte_uren_table = '''
CREATE TABLE IF NOT EXISTS gewerkte_uren (
    id INTEGER PRIMARY KEY,
    datum TEXT,
    uren INTEGER
);
'''

# Uitvoeren van de query's om de tabellen aan te maken
cursor.execute(create_omzet_table)
cursor.execute(create_gewerkte_uren_table)

# Bevestigen en sluiten van de verbinding met de database
conn.commit()
conn.close()
