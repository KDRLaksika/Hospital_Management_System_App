import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=LAPTOP-42R4LMMQ\\SQLEXPRESS;"
        "Database=HospitalDB;"
        "Trusted_Connection=yes;"
    )
    return conn
