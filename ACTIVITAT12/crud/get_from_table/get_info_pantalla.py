from db_connection.connection import create_connection


def get_boto_inici():
    conn = create_connection()
    cur = conn.cursor()

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

    query = "SELECT ABECEDARI FROM INFO_PANTALLA;"

    cur.execute(query)
    abecedari = cur.fetchone()
    abecedari = abecedari[0]

    cur.close()
    conn.close()

    return abecedari