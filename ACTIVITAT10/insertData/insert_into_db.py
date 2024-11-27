import pandas as pd
from db_connect import connection


def insert_data_csv_to_db(pos, data):
    conn = connection.create_connection()
    cur = conn.cursor()

    query = "INSERT INTO PARAULES(WORD, THEME) VALUES(%s, %s);"
    values = (data["WORD"][pos],data["THEME"][pos])

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}

df = pd.read_csv("../paraules_tematica_penjat.csv")
d = df.to_dict(orient='list')

for i in range(500):
    insert_data_csv_to_db(i, d)