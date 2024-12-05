# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2

# Connect to MySQL
mysql_conn = mysql.connector.connect(user='root', password='12345678',host='localhost',database='sales')

# create cursor
mysql_cursor = mysql_conn.cursor()

# Connect to DB2 or PostgreSql
dsn_hostname = '127.0.0.1'
dsn_user='postgres'        # e.g. "abc12345"
# dsn_pwd ='MTM5MzMtbGFrc2ht'      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port ="5432"                # e.g. "50000" 
dsn_database ="softcart"           # i.e. "BLUDB"

# create connection
psql_conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   # password=dsn_pwd,
   host=dsn_hostname, 
   port= dsn_port
)
#Crreate a cursor onject using cursor() method
psql_cursor = psql_conn.cursor()

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
	SQL = "SELECT MAX(rowid) FROM sales_data"
	psql_cursor.execute(SQL)
	last_row_id = psql_cursor.fetchall()
	return last_row_id[0][0]

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	SQL = "SELECT * FROM sales_data WHERE rowid > %s"
	mysql_cursor.execute(SQL, (rowid,))
	latest_records = mysql_cursor.fetchall()
	return latest_records

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.
def insert_records(records):
	SQL = "INSERT INTO sales_data (rowid,product_id,customer_id,quantity) VALUES (%s,%s,%s,%s)"
	psql_cursor.executemany(SQL, records)
	psql_conn.commit()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program