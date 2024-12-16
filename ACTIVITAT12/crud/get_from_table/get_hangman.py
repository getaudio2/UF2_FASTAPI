from db_connection.connection import create_connection

def get_hangman_img():
    conn = create_connection()
    cur = conn.cursor()

    query = "SELECT HANGMAN_IMG FROM HANGMAN;"

    cur.execute(query)
    hangmanimg = cur.fetchone()
    hangmanimg = hangmanimg[0]

    cur.close()
    conn.close()

    return hangmanimg