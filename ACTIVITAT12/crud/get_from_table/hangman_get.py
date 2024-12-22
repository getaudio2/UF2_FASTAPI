from db_connection.connection import create_connection

def get_hangman_img():
    conn = create_connection()
    cur = conn.cursor()

    # Retorna la imatge/nombre d'intents
    query = "SELECT HANGMAN_IMG FROM HANGMAN;"

    cur.execute(query)
    # La taula hangman conté una row i column
    hangmanimg = cur.fetchone() # Agafem la primera row
    hangmanimg = hangmanimg[0] # I la primera columna

    cur.close()
    conn.close()

    return hangmanimg