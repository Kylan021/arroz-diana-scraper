import pandas as pd
import plotly.express as px
from analysis.data_processor import obtener_datos, comparar_precios_actuales, resumen_general


def dashboard_comparativo(df):

    """
    Crea un gráfico de barras comparando el precio actual del Arroz Diana
    entre los diferentes supermercados.
    """

    comparar = comparar_precios_actuales(df)

    if comparar.empty:

        print("[ADVERTENCIA] No hay datos para el gráfico comparativo.")
        return None

    fig = px.bar(

        comparar,
        x="supermercado",
        y="precio",
        color="supermercado",
        text="precio",
        title="Comparativa actual de precios del Arroz Diana (500 g)",
        labels={"precio": "Precio (COP)", "supermercado": "Supermercado"},

    )

    fig.update_traces(texttemplate="%{text:.0f}", textposition="outside")
    fig.update_layout(yaxis_title="Precio (COP)", xaxis_title="Supermercado")

    return fig


def dashboard_historico(df):

    """
    Crea un gráfico de líneas mostrando la evolución del precio a lo largo del tiempo.
    """

    if df.empty:

        print("[ADVERTENCIA] No hay datos históricos para graficar.")

        return None

    df["fecha_scraping"] = pd.to_datetime(df["fecha_scraping"])

    fig = px.line(

        df,
        x="fecha_scraping",
        y="precio",
        color="supermercado",
        markers=True,
        title="Evolución histórica de precios del Arroz Diana (500 g)",
        labels={"fecha_scraping": "Fecha", "precio": "Precio (COP)", "supermercado": "Supermercado"},

    )

    fig.update_layout(xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))

    return fig


def dashboard_promedios(df):

    """
    Crea un gráfico circular (pie chart) con los precios promedio por supermercado.
    """

    resumen = resumen_general(df)

    if resumen.empty:

        print("[ADVERTENCIA] No hay datos para el gráfico de promedios.")

        return None

    fig = px.pie(

        resumen,
        names="supermercado",
        values="precio_promedio",
        title="Promedio de precios del Arroz Diana por supermercado",
        hole=0.3,

    )

    return fig


if __name__ == "__main__":

    df = obtener_datos()

    graficos = {

        "comparativo": dashboard_comparativo(df),
        "historico": dashboard_historico(df),
        "promedios": dashboard_promedios(df),

    }

    for nombre, fig in graficos.items():

        if fig:
            
            fig.write_html(f"data/dashboard_{nombre}.html")
            print(f"[OK] Dashboard '{nombre}' generado en /data")
