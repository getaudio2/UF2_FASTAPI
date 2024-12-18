import psycopg2 as pg
from db_connection.connection import create_connection

def insert_registre_joc(usuari_id):
    try:
        conn = create_connection()
        cur = conn.cursor()

        query = '''INSERT INTO REGISTRE_JOC(USUARI_ID, 
                                            PUNTS_ACTUALS, 
                                            TOTAL_PARTIDES, 
                                            PARTIDES_GUANYADES, 
                                            HIGHSCORE) 
                                            VALUES(%s, %s, %s, %s, %s);
        '''
        values = (usuari_id,8,2,"2 (100%)", "2024-9-12 - 8 punts")

        cur.execute(query, values)
        conn.commit()

        updated_rows = cur.rowcount

        cur.close()
        conn.close()

        return {"Updated rows": updated_rows}
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        cur.close()
        conn.close()