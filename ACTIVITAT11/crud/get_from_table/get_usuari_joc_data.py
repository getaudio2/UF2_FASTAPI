from db_connection.connection import create_connection


def get_usuari_game_data():
    conn = create_connection()
    cur = conn.cursor()

    query = '''SELECT R.PUNTS_ACTUALS,
                        R.TOTAL_PARTIDES,
                        R.PARTIDES_GUANYADES,
                        R.HIGHSCORE
                        FROM REGISTRE_JOC AS R
                        INNER JOIN USUARIS AS U
                        ON U.ID = R.USUARI_ID;
    '''

    cur.execute(query)
    boto = cur.fetchone()

    cur.close()
    conn.close()

    return boto