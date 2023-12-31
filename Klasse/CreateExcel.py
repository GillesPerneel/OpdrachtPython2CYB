import sqlite3
import pandas as pd

# Function to fetch data from the 'omzet' table in the database
def VerkrijgDataEx():
    db_path = 'DB/vb_database.db'  # Path to your SQLite database
    conn = sqlite3.connect(db_path)
    query = "SELECT datum, bedrag FROM omzet"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

# Function to create an Excel file with the fetched data
def CreateExcel(data):
    filename = 'omzet_data.xlsx'  # File name for the Excel file
    data.to_excel(filename, index=False)
    print(f"Excel file '{filename}' created successfully.")

# Fetch data from the database
omzet_data = VerkrijgDataEx()

# Create Excel file with the fetched data
CreateExcel(omzet_data)
