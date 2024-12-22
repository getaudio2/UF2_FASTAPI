from db_connection.connection import create_connection

def update_paraula_secreta(paraulaSecreta):
    conn = create_connection()
    cur = conn.cursor()

    # Substituïm el "Comenzar partida" per la paraula secreta amb "_"
    # No substitueix el botó, sinó el text inicial on anirà la paraula secreta.
    query = "UPDATE INFO_PANTALLA SET paraula_secreta = %s;"
    values = (paraulaSecreta,)

    cur.execute(query, values)
    conn.commit()

    # Comprovem les rows alterades per saber si l'update s'ha fet correctament
    updated_rows = cur.rowcount

    cur.close()
    conn.close()

    return {"Updated rows": updated_rows}