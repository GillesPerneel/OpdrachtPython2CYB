import sqlite3
import csv

# Function to fetch data from the 'omzet' table in the database
def verkrijgDataCSV():
    db_path = 'DB/vb_database.db'  # Path to your SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT datum, bedrag FROM omzet")
    data = cursor.fetchall()

    conn.close()
    return data

# Function to create a CSV file with the fetched data
def CreateCSVMetData(data):
    filename = 'omzet_data.csv'  # File name for the CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Datum', 'Bedrag'])  # Writing header
        writer.writerows(data)
    print(f"CSV file '{filename}' created successfully.")

# Fetch data from the database
omzet_data = verkrijgDataCSV()

# Create CSV file with the fetched data
CreateCSVMetData(omzet_data)