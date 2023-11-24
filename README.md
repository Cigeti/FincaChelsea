# Proyecto Finca Chelsea

## Descripción
Este proyecto se centra en la representación gráfica de datos recopilados por sensores ubicados en la Finca Chelsea. El objetivo es analizar y visualizar de manera efectiva los datos ambientales y del suelo para facilitar una comprensión profunda de las condiciones de la finca, permitiendo una gestión agrícola más informada y eficiente.

Utilizando Python y diversas bibliotecas de visualización, este código transforma datos en bruto en gráficos intuitivos y detallados, destacando tendencias, patrones y correlaciones clave entre las variables medidas por los sensores.

## Características del Proyecto
- Recopilación de Datos: El proyecto procesa datos provenientes de múltiples sensores que registran variables como la humedad, pH del suelo, temperatura, entre otros.
- Visualización de Datos: Se utilizan bibliotecas como Matplotlib y Seaborn para crear gráficos que muestren de manera clara las relaciones entre las diferentes variables.
- Análisis Interactivo: El proyecto está diseñado para ser flexible y adaptable, permitiendo a los usuarios seleccionar diferentes parámetros y rangos de tiempo para el análisis.

## Instalación
Instalación
Para comenzar a usar este proyecto, sigue estos pasos:

- bash
- Copy code
- git clone https://github.com/Cigeti/FincaChelsea.git
- cd FincaChelsea
- pip install -r requirements.txt
Asegúrate de tener Python instalado en tu sistema. Este proyecto depende de varias bibliotecas Python, como Pandas, Numpy, Matplotlib y Seaborn, que se pueden instalar mediante el archivo requirements.txt.

## Uso
Para usar este proyecto, sigue los pasos a continuación:

python
Copy code
import AppFincaChelsea as afc

## Cargar los datos (asegúrate de tener los archivos de datos en las carpetas correspondientes)
datos_ambiente = afc.cargar_datos('NodoAmbiente')
datos_ph = afc.cargar_datos('NodoPH')
datos_suelo = afc.cargar_datos('NodoSuelo')

## Crear y visualizar gráficos
afc.crear_graficos(datos_ambiente, datos_ph, datos_suelo)

## Funcionalidades
- Importación de datos desde múltiples fuentes.
- Creación de gráficos para visualizar relaciones entre humedad, pH, y otras variables del suelo.
- Herramientas personalizables para análisis específicos de datos agrícolas.

## Contribuir
Las contribuciones son bienvenidas. Para contribuir, haz un fork del repositorio, crea una rama con tus mejoras y envía un pull request.
