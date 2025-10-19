from flask import Flask
from flask_cors import CORS
import os


def create_app():

    """
    Crea e inicializa la aplicación Flask.
    Configura rutas, carpetas estáticas y plantillas HTML.
    """

    app = Flask(

        __name__,
        template_folder="templates",
        static_folder="static"

    )

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave_segura_arroz_diana")

    CORS(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    print("[OK] Aplicación Flask inicializada correctamente.")

    return app
