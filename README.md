# Sistema de Análisis del Arroz Diana

Este proyecto implementa un sistema completo de **Análisis y Diseño de Software**, cuyo propósito es automatizar el scraping del producto **Arroz Diana (500g)** en diferentes supermercados colombianos, analizar los precios recolectados, y presentarlos en dashboards interactivos accesibles desde una aplicación web.

---

## Descripción General

El sistema realiza scraping de los siguientes supermercados:

- **Éxito**
- **D1**
- **Megatiendas**
- **Olímpica**
- **La Rebaja Virtual**

Los datos recolectados incluyen:
- Nombre del producto  
- Descripción  
- Precio  
- Si tiene descuento  
- Fecha del scraping  
- Enlace del producto  
- Supermercado de origen

Luego, los datos se almacenan en **MySQL**, se procesan con **Pandas**, se visualizan con **Plotly**, y se exponen mediante una **aplicación Flask**.

---

## Tecnologías Usadas

| Área | Tecnología |
|------|-------------|
| Scraping | Playwright (asíncrono) y BeautifulSoup4 |
| Base de Datos | MySQL |
| Procesamiento de datos | Pandas |
| Visualización | Plotly Express |
| Web App | Flask + Bootstrap |
| Persistencia | Archivos CSV de respaldo |

---

## Estructura del Proyecto

```
arroz_diana_scraper/
│
├── config.py
├── main.py
│
├── database/
│   ├── db_connection.py
│   ├── models.py
│   ├── queries.py
│
├── scraper/
│   ├── base_scraper.py
│   ├── exito_scraper.py
│   ├── d1_scraper.py
│   ├── megatiendas_scraper.py
│   ├── olimpica_scraper.py
│   ├── rebaja_scraper.py
│
├── analysis/
│   ├── data_processor.py
│   ├── dashboards.py
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── controllers.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard_general.html
│   │   ├── dashboard_detalle.html
│
├── data/
│   ├── precios_YYYY-MM-DD_HH-MM-SS.csv
│   ├── resumen_general.csv
│   ├── precios_actuales.csv
│
└── run_flask.py
```

---

## Cómo Ejecutar el Proyecto

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Instalar navegadores de Playwright
```bash
playwright install
```

### Ejecutar scraping
```bash
python main.py
```

Los datos se almacenarán automáticamente en MySQL y en `/data/` como CSV.

### Ejecutar la aplicación web
```bash
python run_flask.py
```
Luego, abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador.

---

## Funcionalidades Principales

| Funcionalidad | Descripción |
|----------------|-------------|
| Scraping automático | Obtiene precios actualizados del Arroz Diana desde varios supermercados. |
| Almacenamiento | Guarda los datos en MySQL y genera copias CSV. |
| Dashboards | Visualiza comparaciones, promedios e históricos de precios. |
| Interfaz Web | Accede fácilmente a la información desde cualquier navegador. |
| Redirección | Permite ir directamente al sitio del supermercado para comprar. |

---

## Desarrollador
**Autores:** Andres Torres, Juan Puello, Sergio Angulo, Jesus Payares y Jorge Narvaez
**Proyecto académico:** Web Scraping  
**Fecha:** 2025-10-19

---

## Licencia
Este proyecto es de uso académico y puede modificarse libremente con fines educativos.
