# ✅ README.md — Análisis de Datos Tributarios con Pruebas Unitarias

## 📌 **Objetivo**

Diseñar, implementar y ejecutar **pruebas unitarias** aplicadas a funciones de análisis de datos tributarios usando Python y un archivo CSV real proporcionado por el SRI (Formulario 104 – periodo fiscal 2024).  
La práctica busca garantizar la confiabilidad de los cálculos y la correcta manipulación de información estructurada.

---

## 🧰 **Herramientas Utilizadas**

- Python 3.10+  
- Editor de código (VSCode)  
- Módulo `unittest`  
- Terminal / Consola  
- Archivo `sri_ventas_2024.csv` (descargado del SRI)  
- Librería `coverage.py` para medir cobertura de código  
- Git y GitHub  

---

## 📂 **Estructura del Proyecto**

laboratorio-3/
│── app.py
│── datos/
│ └── sri_ventas_2024.csv
│── src/
│ └── procesador.py
│── tests/
│ └── test_analizador.py
│── venv/
└── .gitignore


---

## 📝 **Descripción del Proyecto**

El proyecto implementa un analizador de datos contables y tributarios provenientes del SRI.  
El archivo CSV contiene registros mensuales por provincia, cantón y sector económico, con información sobre:

- Ventas  
- Compras  
- Exportaciones  
- Importaciones  
- Tarifas y valores tributarios  

La aplicación permite:

- Obtener el total de ventas por provincia  
- Consultar ventas de una provincia específica  
- Ejecutar pruebas unitarias  
- Calcular cobertura del código  

---

# 🧪 **Actividades Realizadas**

## **1. Preparación del entorno**

- Se creó la estructura base del proyecto.  
- Se descargó el archivo `sri_ventas_2024.csv` desde el SRI.  
- Se creó un repositorio en GitHub y se realizaron commits durante el desarrollo.  

---

## **2. Implementación de la funcionalidad**

En `src/procesador.py` se creó la clase **Analizador**, con las funciones:

### ✔ `ventas_totales_por_provincia()`  
Retorna un diccionario con el total de ventas agrupado por provincia.

### ✔ `ventas_por_provincia(nombre)`  
Retorna el total de ventas de una provincia consultada.

---

## **3. Punto de entrada del programa**

En `app.py` se implementó un menú que:

- Muestra el resumen de ventas por provincia.  
- Solicita una provincia al usuario.  
- Imprime el valor de ventas correspondiente.  

---

## **4. Pruebas unitarias**

En `tests/test_analizador.py` se validó:

✔ Que el total de provincias sea coherente  
✔ Que los valores sean numéricos y no negativos  
✔ Que las funciones retornen diccionarios  
✔ Que las provincias consultadas existan  
✔ Validación de valores de 3 provincias  

---

## **5. Trabajo Autónomo**

Se investigaron y diseñaron extensiones opcionales:

- Exportaciones totales por mes  
- Porcentaje de ventas con tarifa 0%  
- Provincia con mayor volumen de importaciones  

# **TRABAJO EXTRA**

## ** 1. Se descargo el código de git hub**

## **2. Crear un entorno virtual**

- Se creó un entorno virtual llamado `venv` para el proyecto:

-```bash
python -m venv venv

---

## **3. Activar el entorno virtual **

    Se activó el entorno virtual en Linux:

source venv/bin/activate

## ** 4. Instalar coverage **

    Se instaló la librería coverage dentro del entorno virtual:

pip install coverage

## ** 5. Ejecutar Coverage **

    Se ejecutaron las pruebas con cobertura de código:

coverage run -m unittest discover -s tests -p "test_*.py"

    Se generó el reporte en consola:

coverage report

    Se generó el reporte HTML

## ** 6. Actualizar el archivo .gitignore **

    Se actualizó .gitignore para no hacer seguimiento del entorno virtual:

venv/
.env/
.venv/
ENV/

## ** 7. Se genro un Readme **
## ** 8.Se actualizo el repositorio hacineod un push  **
