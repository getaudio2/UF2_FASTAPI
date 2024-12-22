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
        # Com que es tracta del primer insert, aquestes dades haurien de ser les inicials
        # "Id d'usuari", 0, 0, "0 (0%)", "Sense highscore"
        values = (usuari_id,8,2,"2 (100%)", "2024-9-12 - 8 punts") # Dades d'exemple

        cur.execute(query, values)
        conn.commit()

        # Comprovem les rows alterades per saber si s'ha inserit correctament
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