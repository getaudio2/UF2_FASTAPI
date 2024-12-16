import psycopg2 as pg
from db_connection.connection import create_connection

# Executar per crear la taula o crear-la directament al pgadmin
# (Crida de la funció a sota d'aquest fitxer)
def create_table_usuari():
    try:
        # Agafem la conexió a la BBDD de connection.py
        conn = create_connection()
        connection = conn.cursor()

        sql = '''CREATE TABLE IF NOT EXISTS USUARIS(
                        ID serial PRIMARY KEY,
                        USERNAME VARCHAR(40) NOT NULL,
                        PASSWORD VARCHAR(40) NOT NULL
        )'''

        # Enviem la query per crear la taula USERS
        connection.execute(sql)
        # Commit per fer efectius els canvis de la query a la BBDD
        conn.commit()

        return "Taula PARAULES creada correctament"
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        conn.close()

create_table_usuari() # Crida de la funció