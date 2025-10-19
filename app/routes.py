from flask import Blueprint, render_template, redirect, url_for
from analysis.data_processor import obtener_datos, comparar_precios_actuales, resumen_general

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():

    """
    Página principal: muestra la tabla comparativa general.
    """

    df = obtener_datos()
    resumen = resumen_general(df)
    comparar = comparar_precios_actuales(df)

    return render_template("index.html", resumen=resumen.to_dict(orient="records"), comparar=comparar.to_dict(orient="records"))


@main_bp.route("/dashboard")
def dashboard_general():

    """
    Muestra un dashboard general con los precios comparativos y promedios.
    """

    return render_template("dashboard_general.html")


@main_bp.route("/dashboard/<supermercado>")
def dashboard_detalle(supermercado):

    """
    Muestra un dashboard individual por supermercado.
    """

    df = obtener_datos()
    df_super = df[df["supermercado"] == supermercado]

    return render_template("dashboard_detalle.html", supermercado=supermercado, datos=df_super.to_dict(orient="records"))


@main_bp.route("/redirigir/<supermercado>")
def redirigir(supermercado):

    """
    Redirige al usuario a la página web del producto en el supermercado seleccionado.
    """

    df = obtener_datos()
    registro = df[df["supermercado"] == supermercado].sort_values(by="fecha_scraping", ascending=False).head(1)

    if not registro.empty:

        url = registro.iloc[0]["url"]
        
        return redirect(url)

    return redirect(url_for("main.home"))
