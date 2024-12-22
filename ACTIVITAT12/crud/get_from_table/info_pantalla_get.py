from db_connection.connection import create_connection


def get_boto_inici():
    conn = create_connection()
    cur = conn.cursor()

    # Agafem el botó d'inici que diu "Comenzar partida"
    query = "SELECT BOTO_INICI FROM INFO_PANTALLA;"

    cur.execute(query)
    boto = cur.fetchone()
    boto = boto[0]

    cur.close()
    conn.close()

    return boto

def get_paraula_secreta():
    conn = create_connection()
    cur = conn.cursor()

    # Agafem la paraula secreta triada aleatoriament
    # El front rebrà la paraula secreta per mostrar-la amagada amb "_"
    query = "SELECT PARAULA_SECRETA FROM INFO_PANTALLA;"

    cur.execute(query)
    paraula = cur.fetchone()
    paraula = paraula[0]

    cur.close()
    conn.close()

    return paraula

def get_abecedari():
    conn = create_connection()
    cur = conn.cursor()

    # Consulta per rebre les lletres de l'abecedari pels botons al front
    # Útil si es vol triar abecedaris d'altres idiomes guardats a la BBDD
    query = "SELECT ABECEDARI FROM INFO_PANTALLA;"

    cur.execute(query)
    abecedari = cur.fetchone()
    abecedari = abecedari[0]

    cur.close()
    conn.close()

    return abecedari