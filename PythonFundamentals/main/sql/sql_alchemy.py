import sqlalchemy
from sqlalchemy import text

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'ODBC+Driver+17+for+SQL+Server'

# Create a SQLAlchemy engine for connecting to the SQL Server database
engine = sqlalchemy.create_engine(
  f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}"
)

connection = engine.connect()

products = text("SELECT * FROM Products")
results = connection.execute(products)
# for item in results:
#   print(item)
#
print(results.fetchone())
print(results.fetchmany(2))
