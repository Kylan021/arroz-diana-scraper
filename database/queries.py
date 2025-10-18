from database.db_connection import get_connection


def insert_precio(data):

    """
    Inserta un nuevo registro de precio en la tabla precios_arroz.
    :param data: dict con claves:
        supermercado, nombre_producto, descripcion, precio, descuento, fecha_scraping, url
    """

    query = """

        INSERT INTO precios_arroz 
        (supermercado, nombre_producto, descripcion, precio, descuento, fecha_scraping, url)
        VALUES (%s, %s, %s, %s, %s, %s, %s);

    """
    values = (
        
        data["supermercado"],
        data["nombre_producto"],
        data.get("descripcion", ""),
        data["precio"],
        data["descuento"],
        data["fecha_scraping"],
        data["url"]

    )

    conn = get_connection()

    if conn:

        cursor = conn.cursor()

        try:

            cursor.execute(query, values)
            conn.commit()
            print(f"[OK] Registro insertado para {data['supermercado']}")

        except Exception as e:

            print(f"[ERROR] No se pudo insertar el registro: {e}")

        finally:

            cursor.close()
            conn.close()


def get_all_precios():

    """
    Devuelve todos los registros de la tabla precios_arroz.
    """

    query = "SELECT * FROM precios_arroz ORDER BY fecha_scraping DESC;"

    conn = get_connection()
    results = []

    if conn:

        cursor = conn.cursor(dictionary=True)

        try:

            cursor.execute(query)
            results = cursor.fetchall()

        except Exception as e:

            print(f"[ERROR] No se pudo obtener los registros: {e}")

        finally:
            
            cursor.close()
            conn.close()

    return results


def get_precios_by_supermercado(nombre_supermercado):

    """
    Devuelve los registros filtrados por supermercado.
    """

    query = """
        SELECT * FROM precios_arroz
        WHERE supermercado = %s
        ORDER BY fecha_scraping DESC;
    """

    conn = get_connection()
    results = []

    if conn:

        cursor = conn.cursor(dictionary=True)

        try:

            cursor.execute(query, (nombre_supermercado,))
            results = cursor.fetchall()

        except Exception as e:

            print(f"[ERROR] No se pudo obtener datos de {nombre_supermercado}: {e}")

        finally:

            cursor.close()
            conn.close()

    return results


def delete_old_records(days=7):

    """
    Elimina registros con más de X días de antigüedad (por defecto 7 días).
    """

    query = "DELETE FROM precios_arroz WHERE fecha_scraping < NOW() - INTERVAL %s DAY;"
    
    conn = get_connection()

    if conn:

        cursor = conn.cursor()

        try:

            cursor.execute(query, (days,))
            conn.commit()
            print(f"[OK] Registros antiguos eliminados (>{days} días).")

        except Exception as e:

            print(f"[ERROR] No se pudieron eliminar los registros: {e}")

        finally:

            cursor.close()
            conn.close()
