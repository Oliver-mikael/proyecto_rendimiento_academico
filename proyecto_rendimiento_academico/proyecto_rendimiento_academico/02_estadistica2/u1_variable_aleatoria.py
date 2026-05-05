# -*- coding: utf-8 -*-
"""
ARCHIVO   : u1_variable_aleatoria.py
CARPETA   : 02_estadistica2/
MATERIA   : Estadística II — Unidad 1
TEMA      : Variable Aleatoria

PROPÓSITO : Definir formalmente las variables aleatorias del proyecto
            y calcular sus propiedades teóricas (esperanza, varianza).

VARIABLES DEL PROYECTO:
    X1 = horas_estudio  → continua, distribución normal
    X2 = asistencia     → discreta (0-20 clases), binomial → luego continua
    Y  = nota_final     → continua, normal (combinación lineal de X1, X2)

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np

# TODO 1: Calcular esperanza (media) de forma manual
def esperanza(valores, probabilidades=None):
    """
    Si probabilidades=None → calcular como media muestral
    Si probabilidades dadas → E[X] = suma(x_i * p_i)
    """
    pass  # TODO

# TODO 2: Calcular varianza de forma manual
def varianza(valores, probabilidades=None):
    """
    Var[X] = E[X²] - (E[X])²
    """
    pass  # TODO

# TODO 3: Describir cada variable aleatoria del proyecto
# (tipo, parámetros, esperanza teórica, varianza teórica, valor muestral)

if __name__ == "__main__":
    print("=== UNIDAD 1: VARIABLES ALEATORIAS ===\n")
    # TODO: cargar datos desde ../datos/raw/estudiantes.csv
    # TODO: para cada variable, calcular E[X] y Var[X] muestral
    # TODO: comparar con los valores teóricos de la simulación
