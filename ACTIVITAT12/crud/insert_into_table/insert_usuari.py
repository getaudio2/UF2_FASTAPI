from db_connection.connection import create_connection


def insert_usuari():
    conn = create_connection()
    cur = conn.cursor()

    query = "INSERT INTO USUARIS(USERNAME, PASSWORD) VALUES(%s, %s);"
    values = ("Jugador 2", "admin")

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}

insert_usuari()