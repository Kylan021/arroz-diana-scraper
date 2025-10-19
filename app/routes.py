from flask import Blueprint, render_template, redirect, url_for
from app.controllers import (
    obtener_resumen_general,
    generar_dashboard_general,
    generar_dashboard_individual
)

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():

    """
    Página principal con resumen general de precios y comparación actual.
    """

    datos = obtener_resumen_general()

    return render_template(

        "index.html",
        resumen=datos["resumen"],
        comparar=datos["comparar"]

    )


@main_bp.route("/dashboard")
def dashboard_general():

    """
    Muestra el dashboard general con los gráficos comparativos, históricos y de promedios.
    """

    graficos = generar_dashboard_general()

    return render_template("dashboard_general.html", graficos=graficos)


@main_bp.route("/dashboard/<supermercado>")
def dashboard_detalle(supermercado):

    """
    Muestra el dashboard individual con los datos y evolución del supermercado seleccionado.
    """

    dashboard = generar_dashboard_individual(supermercado)
    return render_template(

        "dashboard_detalle.html",
        supermercado=supermercado.capitalize(),
        grafico=dashboard["historico"],
        datos=dashboard["info"]

    )


@main_bp.route("/redirigir/<supermercado>")
def redirigir(supermercado):

    """
    Redirige al usuario a la página real del producto en el supermercado elegido.
    """

    from analysis.data_processor import obtener_datos
    
    df = obtener_datos()
    registro = df[df["supermercado"] == supermercado].sort_values(by="fecha_scraping", ascending=False).head(1)

    if not registro.empty:

        url = registro.iloc[0]["url"]

        return redirect(url)

    return redirect(url_for("main.home"))
