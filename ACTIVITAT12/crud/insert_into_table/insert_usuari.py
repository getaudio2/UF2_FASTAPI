from db_connection.connection import create_connection

def insert_usuari(username, password):
    conn = create_connection()
    cur = conn.cursor()

    query = "INSERT INTO USUARIS(USERNAME, PASSWORD) VALUES(%s, %s);"
    values = (username, password)

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}