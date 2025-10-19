from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper


class RebajaScraper(BaseScraper):
    """
    Extrae información del producto Arroz Diana 500g desde La Rebaja Virtual.
    """

    def parse_html(self):

        soup = BeautifulSoup(self.html, "html.parser")

        nombre_tag = soup.find("span", class_="vtex-store-components-3-x-productBrand")
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else "Nombre no encontrado"

        descripcion_tag = soup.find("div", class_="copservir-larebaja-theme-7-x-accordion__text")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else ""

        precio_tag = soup.find("span", class_="copservir-larebaja-theme-7-x-productPriceValue")
        precio_texto = precio_tag.get_text(strip=True) if precio_tag else "0"
        precio = self._limpiar_precio(precio_texto)

        descuento = False

        return {

            "nombre_producto": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "descuento": descuento

        }


    def _limpiar_precio(self, texto):

        """
        Limpia el texto del precio (quita símbolos, puntos y espacios).
        Ejemplo: "$2.400" -> 2400.0
        """

        try:

            limpio = (

                texto.replace("$", "")
                .replace(" ", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()

            )

            return float(limpio)
        
        except ValueError:
            
            return 0.0
