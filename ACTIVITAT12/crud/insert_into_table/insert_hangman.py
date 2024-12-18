from db_connection.connection import create_connection


def insert_hangman_img(imgUrl):
    conn = create_connection()
    cur = conn.cursor()

    query = "INSERT INTO HANGMAN(HANGMAN_IMG) VALUES(%s);"
    values = (imgUrl,)

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}