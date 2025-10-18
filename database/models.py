from database.db_connection import get_connection

def create_tables():
    """
    Crea la tabla 'precios_arroz' si no existe.
    Contiene los datos obtenidos del scraping.
    """

    query = """

    CREATE TABLE IF NOT EXISTS precios_arroz (

        id INT AUTO_INCREMENT PRIMARY KEY,
        supermercado VARCHAR(100) NOT NULL,
        nombre_producto VARCHAR(150) NOT NULL,
        descripcion TEXT,
        precio DECIMAL(10,2) NOT NULL,
        descuento BOOLEAN DEFAULT FALSE,
        fecha_scraping DATETIME NOT NULL,
        url VARCHAR(255) NOT NULL
        
    );

    """

    conn = get_connection()

    if conn:

        cursor = conn.cursor()

        try:

            cursor.execute(query)
            conn.commit()
            print("[OK] Tabla 'precios_arroz' verificada/creada correctamente.")

        except Exception as e:

            print(f"[ERROR] No se pudo crear la tabla: {e}")

        finally:

            cursor.close()
            conn.close()

    else:

        print("[FALLO] No se pudo conectar a la base de datos.")


if __name__ == "__main__":
    create_tables()
