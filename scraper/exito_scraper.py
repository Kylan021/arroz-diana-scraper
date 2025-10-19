from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper


class ExitoScraper(BaseScraper):

    """
    Extrae información del producto Arroz Diana 500g desde el sitio Éxito.
    """


    def parse_html(self):

        soup = BeautifulSoup(self.html, "html.parser")

        nombre_tag = (

            soup.find("h1") or
            soup.find("span", {"data-testid": "product-name"})

        )

        nombre = nombre_tag.get_text(strip=True) if nombre_tag else "Nombre no encontrado"

        descripcion_tag = soup.find("div", class_="vtex-store-components-3-x-productBrandName")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else ""

        precio_tag = soup.find("p", class_="ProductPrice_container__price__XmMWA ProductPrice_text20__jR3lE")
        precio_texto = precio_tag.get_text(strip=True) if precio_tag else "0"
        precio = self._limpiar_precio(precio_texto)

        descuento_tag = soup.find("div", class_="priceSection_container-promotion_discount__iY3EO")
        descuento = False

        if descuento_tag:

            porcentaje_tag = descuento_tag.find("span", {"data-percentage": "true"})

            if porcentaje_tag:

                descuento = True

        return {

            "nombre_producto": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "descuento": descuento

        }


    def _limpiar_precio(self, texto):

        """
        Limpia el texto del precio (quita símbolos y puntos).
        Ejemplo: "$ 1.940" -> 1940.0
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
