import csv
import datetime
import pyodbc
from decimal import Decimal

# Connect to MSSQL Server
# conn = pymssql.connect(server="DESKTOP-E44RMRQ",
#                        database="cs4354_final")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-E44RMRQ;'
                      'Database=cs4354_final;'
                      'Trusted_Connection=yes;')

# Create a database cursor
cursor = conn.cursor()

print("connection successful")

query = """SELECT c.[company], AVG(c.[comp_benefit_stars]) as company_benifit_stars, m.[early_median_pay]
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company], m.[early_median_pay]"""

# Execute the query
cursor.execute(query)

with open("benifits_pay.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor:
        writer.writerow(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
