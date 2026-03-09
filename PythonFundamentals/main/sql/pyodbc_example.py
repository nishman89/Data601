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
query = cursor.execute("SELECT * FROM Customers")
all_customers = query.fetchall()
for record in all_customers:
    # print(record)
    print(f"Customer Id: {record[0]} - Company Name {record[1]}")

