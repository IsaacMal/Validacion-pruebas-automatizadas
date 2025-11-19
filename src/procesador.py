import csv

class Analizador:
    def __init__(self, ruta_csv):
        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,delimiter= '|')
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        Ejemplo: {'Pichincha': 1000.0, 'Guayas': 2000.5}
        """
        totales = {}

        # Recorremos todas las filas del archivo
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            total_venta = float(fila["TOTAL_VENTAS"])

            # Si la provincia no está en el diccionario, la agregamos
            if provincia not in totales:
                totales[provincia] = total_venta
            else:
                # Si ya existe, sumamos el valor
                totales[provincia] += total_venta

        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        Ejemplo: ventas_por_provincia("Guayas") -> 2000.5
        """
        totales = self.ventas_totales_por_provincia()

        # Verificamos si la provincia está en los totales
        if nombre in totales:
            return totales[nombre]
        else:
            return 0.0


    #Exportaciones totales por mes: sumar EXPORTACIONES agrupadas por MES.
    def exportaciones_totales_por_mes(self):
        """Suma las exportaciones agrupadas por MES."""
        totales = {}
        for fila in self.datos:
            mes = fila.get("MES")
            valor = float(fila.get("EXPORTACIONES", 0))
            totales[mes] = totales.get(mes, 0) + valor
        return totales


    #Porcentaje de ventas con tarifa 0% respecto al total: calcular promedio de (VENTAS_NETAS_TARIFA_0 / TOTAL_VENTAS) * 100 por provincia o sector.
    def porcentaje_ventas_tarifa_0(self):
        """
        Calcula (VENTAS_NETAS_TARIFA_0 / TOTAL_VENTAS) * 100
        y devuelve el promedio por PROVINCIA.
        """
        acumulado = {}
        conteo = {}

        for fila in self.datos:
            prov = fila.get("PROVINCIA")
            tarifa0 = float(fila.get("VENTAS_NETAS_TARIFA_0", 0))
            total = float(fila.get("TOTAL_VENTAS", 0))

            if total == 0:
                continue

            porcentaje = (tarifa0 / total) * 100
            acumulado[prov] = acumulado.get(prov, 0) + porcentaje
            conteo[prov] = conteo.get(prov, 0) + 1

        return {p: acumulado[p] / conteo[p] for p in acumulado}
    

    #Provincia con mayor volumen de importaciones: identificar la provincia con el mayor total de IMPORTACIONES.
    def provincia_mayor_importacion(self):
        """Devuelve la provincia que tiene mayor total de IMPORTACIONES."""
        totales = {}
        for fila in self.datos:
            prov = fila.get("PROVINCIA")
            valor = float(fila.get("IMPORTACIONES", 0))
            totales[prov] = totales.get(prov, 0) + valor

        if not totales:
            return None

        return max(totales, key=totales.get)