from playwright.async_api import async_playwright
from datetime import datetime
from config import SCRAPING_TIMEOUT, HEADLESS_MODE, DATE_FORMAT


class BaseScraper:
    """
    Clase base para los scrapers de supermercados.
    Permite obtener el HTML de una página y extraer datos con BS4.
    """

    def __init__(self, nombre_supermercado, url):

        self.nombre_supermercado = nombre_supermercado
        self.url = url
        self.html = None


    async def get_html(self):

        """
        Usa Playwright para obtener el HTML completo de una página.
        Retorna el contenido HTML.
        """

        print(f"[INFO] Iniciando scraping de {self.nombre_supermercado}...")

        async with async_playwright() as p:

            browser = await p.chromium.launch(headless=HEADLESS_MODE)
            page = await browser.new_page()

            try:

                await page.goto(self.url, timeout=SCRAPING_TIMEOUT * 1000)
                await page.wait_for_timeout(3000)
                self.html = await page.content()
                print(f"[OK] HTML obtenido para {self.nombre_supermercado}")

            except Exception as e:

                print(f"[ERROR] No se pudo obtener HTML de {self.nombre_supermercado}: {e}")

            finally:

                await browser.close()

        return self.html
    

    def parse_html(self):

        """
        Método genérico que debe ser sobrescrito por cada scraper específico.
        Debe devolver un diccionario con los datos del producto.
        """

        raise NotImplementedError("Debes implementar el método parse_html() en el scraper específico.")
    

    async def run(self):

        """
        Ejecuta el flujo completo: obtener HTML + parsear datos.
        Devuelve un diccionario listo para insertar en la base de datos.
        """

        await self.get_html()

        if not self.html:

            return None

        data = self.parse_html()

        data["supermercado"] = self.nombre_supermercado
        data["fecha_scraping"] = datetime.now().strftime(DATE_FORMAT)
        data["url"] = self.url

        return data
