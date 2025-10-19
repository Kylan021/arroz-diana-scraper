from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper


class MegatiendasScraper(BaseScraper):

    """
    Extrae información del producto Arroz Diana 500g desde Megatiendas.
    """

    def parse_html(self):

        soup = BeautifulSoup(self.html, "html.parser")

        nombre_tag = (

            soup.find("h1") or 
            soup.find("span", {"data-testid": "product-name"})

        )

        nombre = nombre_tag.get_text(strip=True) if nombre_tag else "Nombre no encontrado"

        descripcion_tag = soup.find("div", class_="vtex-store-components-3-x-descripcionLarga")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else ""

        precio_tag = (

            soup.find("span", {"data-testid": "price-value"}) or
            soup.find("span", class_="vtex-product-price-1-x-sellingPriceValue")

        )

        precio_texto = precio_tag.get_text(strip=True) if precio_tag else "0"
        precio = self._limpiar_precio(precio_texto)

        descuento_tag = soup.find("span", class_="vtex-product-price-1-x-listPriceValue")
        descuento = bool(descuento_tag and precio < self._limpiar_precio(descuento_tag.text))

        return {

            "nombre_producto": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "descuento": descuento

        }


    def _limpiar_precio(self, texto):

        """
        Limpia el texto del precio (quita símbolos y puntos).
        Ejemplo: "$ 2.890" → 2890.0
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
