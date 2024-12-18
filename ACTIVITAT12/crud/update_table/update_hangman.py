from db_connection.connection import create_connection


def update_hangman_img(imgUrl):
    conn = create_connection()
    cur = conn.cursor()

    query = "UPDATE HANGMAN SET HANGMAN_IMG = %s;"
    values = (imgUrl,)

    cur.execute(query, values)
    conn.commit()

    updated_rows = cur.rowcount

    cur.close()
    conn.close()

    return {"Updated rows": updated_rows}