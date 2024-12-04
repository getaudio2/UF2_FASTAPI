from connection import create_connection


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