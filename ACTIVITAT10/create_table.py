import psycopg2 as pg
from connection import create_connection

def create_table():
    try:
        # Agafem la conexió a la BBDD de connection.py
        conn = create_connection()
        connection = conn.cursor()

        sql = '''CREATE TABLE PARAULES(
                        WORD VARCHAR(255) NOT NULL,
                        THEME VARCHAR(255) NOT NULL
        )'''

        # Enviem la query per crear la taula USERS
        connection.execute(sql)
        # Commit per fer efectius els canvis de la query a la BBDD
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        conn.close()

create_table()