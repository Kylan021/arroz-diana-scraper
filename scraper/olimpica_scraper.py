from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper


class OlimpicaScraper(BaseScraper):
    """
    Extrae información del producto Arroz Diana 500g desde Olímpica.
    """

    def parse_html(self):

        soup = BeautifulSoup(self.html, "html.parser")

        nombre_tag = (

            soup.find("h1") or
            soup.find("span", {"data-testid": "product-name"})

        )

        nombre = nombre_tag.get_text(strip=True) if nombre_tag else "Nombre no encontrado"

        descripcion_tag = soup.find("div", class_="vtex-store-components-3-x-content h-auto")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else ""

        precio_contenedor = soup.find("span", class_="olimpica-dinamic-flags-0-x-currencyContainer")
        precio_texto = ""

        if precio_contenedor:

            spans = precio_contenedor.find_all("span")
            precio_texto = "".join([s.get_text() for s in spans if s.get_text().strip()])

        else:

            precio_texto = "0"

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
        Limpia el texto del precio (quita símbolos, espacios y puntos).
        Ejemplo: "$ 2.200" -> 2200.0
        """
        
        try:

            limpio = (

                texto.replace("$", "")
                .replace("&nbsp;", "")
                .replace(" ", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()

            )

            return float(limpio)
        
        except ValueError:

            return 0.0
