import sqlite3
import csv

# Function to fetch all data from the 'omzet' table in the database
def get_omzet_data():
    db_path = 'DB/vb_database.db'  # Path to your SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM omzet")
    data = cursor.fetchall()

    conn.close()
    return data

# Function to export fetched data to a CSV file
def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Datum', 'Bedrag'])  # Writing header
        writer.writerows(data)

    print(f"Data exported to '{filename}' successfully.")

