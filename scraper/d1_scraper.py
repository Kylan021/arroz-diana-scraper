from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper


class D1Scraper(BaseScraper):

    """
    Extrae información del producto Arroz Diana 500g desde Tiendas D1.
    """

    def parse_html(self):

        soup = BeautifulSoup(self.html, "html.parser")

        nombre_tag = soup.find("h2")

        nombre = (

            nombre_tag.get_text(strip=True).replace("Nombre del producto:", "").strip()
            if nombre_tag else "Nombre no encontrado"

        )

        descripcion_tag = nombre_tag.find_next("p") if nombre_tag else None

        if descripcion_tag and descripcion_tag.find_next("p"):

            descripcion = descripcion_tag.find_next("p").get_text(strip=True)

        else:

            descripcion = ""

        precio_tag = soup.find("p", class_="DetailBasePrice__DetailBasePriceStyles-sc-1hromxy-0 eUWHDQ base__price")
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
        Limpia el texto del precio (quita símbolos y puntos).
        Ejemplo: "$ 1.990" -> 1990.0
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
