import connection

def read_words_by_theme(theme):
    conn = connection.create_connection()
    cur = conn.cursor()

    query = "SELECT WORD FROM PARAULES WHERE THEME = %s;"
    value = (theme,)
    cur.execute(query, value)
    word = cur.fetchall()

    cur.close()
    conn.close()

    return word