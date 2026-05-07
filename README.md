Lenguaje Python fastAPI[standard]

## Instalar dependencias

Desde la raíz del proyecto: poetry install y si no funciona poetry install --no-root

## Ejecutar API

poetry run fastapi dev app/main.py

## Agrear archivo .env en la raiz del proyecto con la siguiente estrucutra

ODOO_URL=
ODOO_DB=
ODOO_USER=
ODOO_PASSWORD=

PRESTASHOP_URL=http://localhost:8081/api
API_KEY=

WP_URL=
WP_CONSUMER_KEY=
WP_CONSUMER_SECRET=