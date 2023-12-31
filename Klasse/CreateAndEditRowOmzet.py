import sqlite3
import os


def add_to_omzet(datum, bedrag):
    
    db_path = 'DB/vb_database.db'
  
    # Verbinding maken met de database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query om een rij toe te voegen aan de tabel 'omzet'
    insert_query = '''
    INSERT INTO omzet (datum, bedrag)
    VALUES (?, ?);
    '''

    # Uitvoeren van de query om de nieuwe rij toe te voegen
    try:
        cursor.execute(insert_query, (datum, bedrag))
        conn.commit()
        print("Rij toegevoegd aan de tabel 'omzet'.")
    except sqlite3.Error as e:
        print(f"Fout bij toevoegen van rij: {e}")

    # Sluiten van de verbinding met de database
    conn.close()

# Function to edit a row in the 'omzet' table based on ID
def edit_row_omzet(row_id, new_datum, new_bedrag):
    db_path = 'DB/vb_database.db'
    if not os.path.exists(db_path):
        print("Database does not exist.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    update_query = '''
    UPDATE omzet
    SET datum = ?,
        bedrag = ?
    WHERE id = ?;
    '''

    try:
        cursor.execute(update_query, (new_datum, new_bedrag, row_id))
        conn.commit()
        print(f"Rij met ID {row_id} bijgewerkt in de 'omzet' tabel.")
    except sqlite3.Error as e:
        print(f"Fout bij bijwerken van de rij: {e}")


    conn.close()