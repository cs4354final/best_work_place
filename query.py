import csv
import datetime
import pyodbc
from decimal import Decimal

# Connect to MSSQL Server
# conn = pymssql.connect(server="DESKTOP-E44RMRQ",
#                        database="cs4354_final")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-E44RMRQ;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

# Create a database cursor
cursor = conn.cursor()

print("connection successful")

query = """SELECT * FROM [master].[dbo].[MSreplication_options]"""

# Execute the query
cursor.execute(query)

with open("output.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor:
        writer.writerow(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
