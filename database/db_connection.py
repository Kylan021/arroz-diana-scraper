import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def get_connection():

    try:

        connection = mysql.connector.connect(

            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"]

        )

        if connection.is_connected():

            return connection

    except Error as e:

        print(f"[ERROR] No se pudo conectar a MySQL: {e}")
        return None


def test_connection():

    conn = get_connection()

    if conn:

        print("[OK] Conexión exitosa a la base de datos.")
        conn.close()

    else:

        print("[FALLO] No se logró conectar a la base de datos.")


if __name__ == "__main__":
    
    test_connection()
