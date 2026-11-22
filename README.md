# Práctica 2 - Selenium WebDriver con Python

## Requisitos
- Windows, Python 3.10+ y Google Chrome actualizado.
- Internet para acceder a https://automationexercise.com.

## Ejecución en PowerShell
```powershell
cd "RUTA_DE_LA_CARPETA\Practica_2_Selenium_WebDriver"
py -m pip install -r requirements.txt
py test_practica2.py
```
Selenium 4 gestiona ChromeDriver automáticamente mediante Selenium Manager en entornos compatibles.

## Casos
- Login incorrecto: mensaje de error y permanencia en `/login`.
- Búsqueda de productos: título de resultados y al menos un producto cuyo nombre contenga `top`.
- Suscripción: mensaje de confirmación y visibilidad del aviso.

## Evidencias
Cada prueba aprobada genera una captura en `evidencias/`. Si falla, revise el error en la terminal; no se debe reportar PASS sin ejecución. Para el informe, capture también la terminal con el resultado de las tres pruebas. Si la web muestra publicidad o tarda en cargar, reintente después de verificar que la página responde.

Localizadores utilizados: ID, NAME, XPATH y CSS_SELECTOR.
