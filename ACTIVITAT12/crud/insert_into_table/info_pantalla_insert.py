from db_connection.connection import create_connection

def insert_info_pantalla():
    conn = create_connection()
    cur = conn.cursor()

    # Inserim els valors per defecte, els textos a renderitzar al front
    # No cal base model ja que només son valors estàtics (excepte paraula secreta, que tindrà PUT)
    query = "INSERT INTO INFO_PANTALLA(BOTO_INICI, PARAULA_SECRETA, ABECEDARI) VALUES(%s, %s, %s);"
    values = ("Començar partida", "Començar partida", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}