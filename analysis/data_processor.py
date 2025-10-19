import pandas as pd
from database.db_connection import get_connection


def obtener_datos():

    """
    Carga todos los registros de precios desde la base de datos MySQL.
    Retorna un DataFrame de Pandas.
    """

    try:

        conn = get_connection()
        query = "SELECT supermercado, nombre_producto, descripcion, precio, descuento, fecha_scraping, url FROM precios_arroz"
        df = pd.read_sql(query, conn)
        conn.close()

        print("[OK] Datos cargados desde la base de datos.")

        return df
    
    except Exception as e:

        print(f"[ERROR] No se pudieron obtener los datos: {e}")

        return pd.DataFrame()


def resumen_general(df):

    """
    Genera un resumen con el precio promedio y máximo por supermercado.
    """

    if df.empty:

        print("[ADVERTENCIA] No hay datos para analizar.")
        return pd.DataFrame()

    resumen = (

        df.groupby("supermercado")
        .agg(

            precio_promedio=("precio", "mean"),
            precio_minimo=("precio", "min"),
            precio_maximo=("precio", "max"),
            con_descuento=("descuento", "sum"),
            total_registros=("precio", "count")

        )
        .reset_index()

    )

    print("[OK] Resumen general generado.")
    return resumen


def comparar_precios_actuales(df):

    """
    Retorna el precio más reciente de cada supermercado para comparar actualizaciones.
    """

    if df.empty:

        print("[ADVERTENCIA] No hay datos para comparar.")
        return pd.DataFrame()

    df["fecha_scraping"] = pd.to_datetime(df["fecha_scraping"])
    df_ordenado = df.sort_values(by=["supermercado", "fecha_scraping"], ascending=[True, False])
    recientes = df_ordenado.groupby("supermercado").head(1).reset_index(drop=True)

    print("[OK] Comparación de precios actuales generada.")
    return recientes[["supermercado", "precio", "fecha_scraping", "url"]]


def generar_reporte_csv(df, resumen, comparar):

    """
    Genera un archivo CSV con los resultados del análisis.
    """

    try:

        resumen.to_csv("data/resumen_general.csv", index=False, encoding="utf-8-sig")
        comparar.to_csv("data/precios_actuales.csv", index=False, encoding="utf-8-sig")
        df.to_csv("data/historico_completo.csv", index=False, encoding="utf-8-sig")

        print("[OK] Reportes CSV generados en /data")

    except Exception as e:

        print(f"[ERROR] No se pudo exportar el reporte: {e}")


if __name__ == "__main__":

    df = obtener_datos()
    resumen = resumen_general(df)
    comparar = comparar_precios_actuales(df)
    generar_reporte_csv(df, resumen, comparar)
