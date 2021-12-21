import psycopg2
import pandas.io.sql as sqlio

conn = psycopg2.connect(
    dbname='dbname',
    user='dbuser',
    password='dbpwd',
    host='localhost',
    port='15432'
)
cursor = conn.cursor()
df = sqlio.read_sql_query('SELECT * FROM hashtags_relation', conn)

cursor.close()
conn.close()
