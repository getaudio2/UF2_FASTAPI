import psycopg2 as pg
from db_connect.connection import create_connection

def read_all():
    try:
        conn = create_connection()
        connection = conn.cursor()

        query = "SELECT * FROM USERS;"

        connection.execute(query)

        # Agafem les rows resultants de la query
        usuaris = connection.fetchall()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()

    # Retornem els usuaris per mostrar-los per pantalla
    return usuaris