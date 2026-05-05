# -*- coding: utf-8 -*-
"""
ARCHIVO   : u3_dist_muestrales.py
MATERIA   : Estadística II — Unidad 3
TEMA      : Distribuciones Muestrales

PROPÓSITO : Demostrar el Teorema Central del Límite con los datos del proyecto.
            Verificar que la media muestral de notas sigue distribución normal.

AUTOR     : [Tu nombre]   FECHA: [Fecha]
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: Distribución de medias muestrales
def distribucion_media_muestral(poblacion, n_muestra, n_repeticiones=1000):
    """
    Toma n_repeticiones muestras de tamaño n_muestra.
    Retorna el array de medias muestrales.
    """
    pass  # TODO

# TODO 2: Graficar histograma de medias (debe ser normal por el TCL)

if __name__ == "__main__":
    print("=== UNIDAD 3: DISTRIBUCIONES MUESTRALES ===\n")
    # TODO: cargar notas desde ../datos/raw/estudiantes.csv
    # TODO: demostrar TCL con n = 5, 15, 30
    # TODO: calcular error estándar = desv_std / sqrt(n)
