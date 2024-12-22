import psycopg2 as pg
from db_connection.connection import create_connection

def delete_usuari(id):
    try:
        conn = create_connection()
        cur = conn.cursor()

        # Query per esborrar l'usuari segons l'id
        query = "DELETE FROM USUARIS WHERE ID = %s;"
        values = (id,)

        cur.execute(query, values)
        conn.commit()

        # Comprovem les rows alterades per saber si l'update s'ha fet correctament
        updated_rows = cur.rowcount

        return {"Rows updated": updated_rows}
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        cur.close()
        conn.close()