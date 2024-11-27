import connection

def read_themes():
    conn = connection.create_connection()
    cur = conn.cursor()

    query = "SELECT DISTINCT THEME FROM PARAULES;"

    cur.execute(query)
    themes = cur.fetchall()

    cur.close()
    conn.close()

    return themes