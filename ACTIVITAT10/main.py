import pandas as pd
import psycopg2 as pg
import connection

df = pd.read_csv("paraules_tematica_penjat.csv")
d = df.to_dict("index")
print(d)

'''
conn = connection.create_connection()
cur = conn.cursor()

query = "INSERT INTO PARAULES(WORD, THEME) VALUES(%s, %s);"

conn.execute(query)
'''