import pyodbc

for item in pyodbc.drivers():
    print(item)

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn = pyodbc.connect(
  'DRIVER={ODBC Driver 17 for SQL Server};'
  f'SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Customers")
print(cursor.fetchall())