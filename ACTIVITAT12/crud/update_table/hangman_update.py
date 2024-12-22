from db_connection.connection import create_connection


def update_hangman_img(imgUrl):
    conn = create_connection()
    cur = conn.cursor()

    # Cada cop que el jugador s'equivoqui, es realitzarà aquesta consulta
    query = "UPDATE HANGMAN SET HANGMAN_IMG = %s;"
    values = (imgUrl,)

    cur.execute(query, values)
    conn.commit()

    # Comprovem les rows alterades per saber si l'update s'ha fet correctament
    updated_rows = cur.rowcount

    cur.close()
    conn.close()

    return {"Updated rows": updated_rows}