import sqlite3
import pandas as pd

# Function to retrieve data from the 'omzet' table in the database
def get_omzet_dataExcel():
    db_path = 'DB/vb_database.db'  # Path to your SQLite database
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM omzet"  # Modify the query according to your table structure
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

# Function to export fetched data to an Excel file
def export_to_excel(data, filename):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')  # 'openpyxl' can be used as well
    data.to_excel(writer, index=False, sheet_name='Omzet Data')  # Modify sheet name as needed
    writer.close()
    print(f"Data exported to '{filename}' successfully.")

