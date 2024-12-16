from db_connection.connection import create_connection

def insert_registre_joc():
    conn = create_connection()
    cur = conn.cursor()

    query = '''INSERT INTO REGISTRE_JOC(USUARI_ID, 
                                        PUNTS_ACTUALS, 
                                        TOTAL_PARTIDES, 
                                        PARTIDES_GUANYADES, 
                                        HIGHSCORE) 
                                        VALUES(%s, %s, %s, %s, %s);
    '''
    values = (2,8,2,"2 (100%)", "2024-9-12 - 8 punts")

    cur.execute(query, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted correctly"}

insert_registre_joc()