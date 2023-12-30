import sqlite3
import os

# Function to add a row to the 'gewerkte_uren' table
def add_to_gewerkte_uren(datum, uren):
    db_path = 'DB/vb_database.db'
    if not os.path.exists(db_path):
        print("Database does not exist.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO gewerkte_uren (datum, uren)
    VALUES (?, ?);
    '''

    try:
        cursor.execute(insert_query, (datum, uren))
        conn.commit()
        print("Rij toegevoegd aan de 'gewerkte_uren' tabel.")
    except sqlite3.Error as e:
        print(f"Fout bij toevoegen van rij: {e}")


    conn.close()

# Function to edit a row in the 'gewerkte_uren' table based on ID
def edit_row_gewerkte_uren(row_id, new_datum, new_uren):
    db_path = 'DB/vb_database.db'
    if not os.path.exists(db_path):
        print("Database does not exist.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    update_query = '''
    UPDATE gewerkte_uren
    SET datum = ?,
        uren = ?
    WHERE id = ?;
    '''

    try:
        cursor.execute(update_query, (new_datum, new_uren, row_id))
        conn.commit()
        print(f"Rij met ID {row_id} bijgewerkt in de 'gewerkte_uren' tabel.")
    except sqlite3.Error as e:
        print(f"Fout bij bijwerken van rij: {e}")


    conn.close()