import psycopg2 as pg
from db_connection.connection import create_connection

def update_registre_joc(id, punts, totalPartides, partidesGuanyades, highscore):
    try:
        conn = create_connection()
        cur = conn.cursor()

        # Aquesta query ens permet actualitzar les dades del jugador
        # cada cop que guanya punts o la partida. Fem servir BaseModel
        query = '''UPDATE REGISTRE_JOC
                    SET PUNTS_ACTUALS = %s, TOTAL_PARTIDES = %s, 
                        PARTIDES_GUANYADES = %s, HIGHSCORE = %s
                    WHERE USUARI_ID = %s;
        '''
        values = (punts,totalPartides,partidesGuanyades, highscore, id)

        cur.execute(query, values)
        conn.commit()

        # Comprovem les rows alterades per saber si l'update s'ha fet correctament
        updated_rows = cur.rowcount

        cur.close()
        conn.close()

        return {"Rows updated": updated_rows}
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        cur.close()
        conn.close()