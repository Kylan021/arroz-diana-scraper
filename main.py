import asyncio
import pandas as pd
from datetime import datetime

from config import URLS_SUPERMERCADOS, DATA_DIR
from database.queries import insert_precio
from scraper.exito_scraper import ExitoScraper
from scraper.d1_scraper import D1Scraper
from scraper.megatiendas_scraper import MegatiendasScraper
from scraper.olimpica_scraper import OlimpicaScraper
from scraper.rebaja_scraper import RebajaScraper


async def ejecutar_scraper(scraper_class, nombre, url):

    """
    Ejecuta un scraper específico y devuelve los datos obtenidos.
    """

    scraper = scraper_class(nombre, url)
    data = await scraper.run()

    if data:

        print(f"[OK] Datos extraídos de {nombre}: {data}")
        insert_precio(data)
        return data
    
    else:

        print(f"[ERROR] No se obtuvieron datos de {nombre}.")
        return None


async def main():

    print("========================================")
    print("   SISTEMA DE ANÁLISIS - ARROZ DIANA")
    print("========================================\n")

    scrapers = [

        (ExitoScraper, "exito", URLS_SUPERMERCADOS["exito"]),
        (D1Scraper, "d1", URLS_SUPERMERCADOS["d1"]),
        (MegatiendasScraper, "megatiendas", URLS_SUPERMERCADOS["megatiendas"]),
        (OlimpicaScraper, "olimpica", URLS_SUPERMERCADOS["olimpica"]),
        (RebajaScraper, "larebaja", URLS_SUPERMERCADOS["larebaja"]),

    ]

    resultados = []

    for scraper_class, nombre, url in scrapers:

        print(f"\n[INFO] Ejecutando scraper: {nombre.upper()}")
        data = await ejecutar_scraper(scraper_class, nombre, url)

        if data:

            resultados.append(data)

    if resultados:

        df = pd.DataFrame(resultados)
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        csv_path = f"{DATA_DIR}/precios_{fecha}.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")

        print(f"\n[OK] Datos exportados a CSV: {csv_path}")

    else:

        print("\n[ADVERTENCIA] No se obtuvieron resultados válidos.")

    print("\nProceso finalizado.")


if __name__ == "__main__":
    asyncio.run(main())
