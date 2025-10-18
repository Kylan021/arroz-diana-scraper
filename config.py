import os
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "0623",
    "database": "arroz_diana",
    "port": 3306
}

URLS_SUPERMERCADOS = {
    "exito": "https://www.exito.com/arroz-diana-500-gr-479512/p",
    "d1": "https://domicilios.tiendasd1.com/p/arroz-diana-500-g-12002073",
    "megatiendas": "https://www.megatiendas.co/arroz-diana-x-500-g-7702511000014/p",
    "olimpica": "https://www.olimpica.com/arroz-diana-500-gr-7702511000014-518231/p",
    "larebaja": "https://www.larebajavirtual.com/arroz-diana-31185/p"
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(DATA_DIR, "logs")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
CURRENT_DATE = datetime.now().strftime(DATE_FORMAT)

SCRAPING_TIMEOUT = 15
HEADLESS_MODE = True 

DASHBOARD_TITLE = "Análisis de precios - Arroz Diana 500g"
REFRESH_INTERVAL = 3600
