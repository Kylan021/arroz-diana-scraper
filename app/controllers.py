from analysis.data_processor import obtener_datos, resumen_general, comparar_precios_actuales
from analysis.dashboards import dashboard_comparativo, dashboard_historico, dashboard_promedios


def obtener_resumen_general():

    """
    Devuelve los datos generales procesados desde la base de datos.
    Incluye el resumen y la comparación actual.
    """

    df = obtener_datos()

    if df.empty:

        return {"resumen": [], "comparar": []}

    resumen = resumen_general(df).to_dict(orient="records")
    comparar = comparar_precios_actuales(df).to_dict(orient="records")

    return {"resumen": resumen, "comparar": comparar}


def generar_dashboard_general():

    """
    Genera los dashboards principales (comparativo, histórico y promedios).
    Devuelve los gráficos en formato HTML para incrustar en la web.
    """

    df = obtener_datos()

    if df.empty:

        return {"comparativo": "", "historico": "", "promedios": ""}

    graficos = {

        "comparativo": dashboard_comparativo(df).to_html(full_html=False) if dashboard_comparativo(df) else "",
        "historico": dashboard_historico(df).to_html(full_html=False) if dashboard_historico(df) else "",
        "promedios": dashboard_promedios(df).to_html(full_html=False) if dashboard_promedios(df) else ""

    }

    return graficos


def generar_dashboard_individual(supermercado):

    """
    Genera un dashboard individual para un supermercado específico.
    Muestra su evolución de precios y estadísticas.
    """

    df = obtener_datos()

    df_super = df[df["supermercado"] == supermercado]

    if df_super.empty:
        
        return {"historico": "", "info": []}

    grafico = dashboard_historico(df_super).to_html(full_html=False) if dashboard_historico(df_super) else ""
    info = df_super.sort_values(by="fecha_scraping", ascending=False).to_dict(orient="records")

    return {"historico": grafico, "info": info}
