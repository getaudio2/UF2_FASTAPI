from db_connection.connection import create_connection

def insert_registre_joc(id, punts, totalPartides, partidesGuanyades, highscore):
    conn = create_connection()
    cur = conn.cursor()

    query = '''UPDATE REGISTRE_JOC
                SET PUNTS_ACTUALS = %s, TOTAL_PARTIDES = %s, 
                    PARTIDES_GUANYADES = %s, HIGHSCORE = %s
                WHERE USUARI_ID = %s;
    '''
    values = (punts,totalPartides,partidesGuanyades, highscore, id)

    cur.execute(query, values)
    conn.commit()

    updated_rows = cur.rowcount

    cur.close()
    conn.close()

    return {"Rows updated": updated_rows}