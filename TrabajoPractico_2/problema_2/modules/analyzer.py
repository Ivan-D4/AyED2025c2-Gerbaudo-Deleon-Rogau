# -*- coding: utf-8 -*-

# analyzer.py

def calcular_promedio_temperaturas(db, fecha1, fecha2):
    temperaturas = db.devolver_temperaturas(fecha1, fecha2)
    if not temperaturas:
        return None
    total = sum(float(temp.split(": ")[1].replace(" ºC", "")) for temp in temperaturas)
    return total / len(temperaturas)

def generar_reporte_temperaturas(db, fecha1, fecha2):
    temperaturas = db.devolver_temperaturas(fecha1, fecha2)
    if not temperaturas:
        return "No hay datos disponibles para el rango de fechas especificado."
    
    max_temp = db.max_temp_rango(fecha1, fecha2)
    min_temp = db.min_temp_rango(fecha1, fecha2)
    promedio = calcular_promedio_temperaturas(db, fecha1, fecha2)
    
    reporte = f"Reporte de temperaturas desde {fecha1} hasta {fecha2}:\n"
    reporte += f"Temperaturas registradas:\n" + "\n".join(temperaturas) + "\n"
    reporte += f"Temperatura máxima: {max_temp} ºC\n"
    reporte += f"Temperatura mínima: {min_temp} ºC\n"
    reporte += f"Temperatura promedio: {promedio:.2f} ºC\n" if promedio is not None else "No se pudo calcular la temperatura promedio.\n"
    
    return reporte