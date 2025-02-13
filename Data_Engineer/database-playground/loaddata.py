import os
import psycopg2
pgpassword = "1"
conn = None
try:
    conn = psycopg2.connect(
        user = "postgres",
        password = pgpassword,
        host = "localhost",
        port = "5432",
        database = "Practice")
except Exception as e:
    print("Error connecting to data warehouse")
    print(e)
else:
    print("Successfully connected to warehouse")
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed")

cur = conn.cursor()

def insert(csv, table):
    # Open CSV file
    with open(csv, 'r') as f:
        next(f)  # Skip the header row
        cur.copy_from(f, table, sep=',')

# insert('DimDate.csv','mydimdate')
insert('DimTruck.csv','mydimwaste')
# insert('DimStation.csv','mydimzone')
insert('FactTrips.csv','myfacttrips')

# Commit and close connection
conn.commit()
cur.close()
conn.close()
