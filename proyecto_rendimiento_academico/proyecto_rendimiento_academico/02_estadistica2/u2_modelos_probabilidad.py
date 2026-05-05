# -*- coding: utf-8 -*-
"""
ARCHIVO   : u2_modelos_probabilidad.py
CARPETA   : 02_estadistica2/
MATERIA   : Estadística II — Unidad 2
TEMA      : Modelos de Probabilidad

DISTRIBUCIONES USADAS EN EL PROYECTO:
    - Normal      → notas (continua, campana de Gauss)
    - Binomial    → asistencia (discreta, éxito/fracaso por clase)
    - Poisson     → número de estudiantes que aprueban por día/semana

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: Distribución Normal — P(X <= x) manual (usando tabla Z o scipy)
def prob_normal(x, media, desv_std):
    """ P(X <= x) para X ~ N(media, desv_std) """
    pass  # TODO

# TODO 2: Distribución Binomial — P(X = k)
def prob_binomial(k, n, p):
    """ P(X = k) para X ~ Bin(n, p) → (n sobre k) * p^k * (1-p)^(n-k) """
    pass  # TODO

# TODO 3: Distribución de Poisson — P(X = k)
def prob_poisson(k, lamda):
    """ P(X = k) para X ~ Poisson(λ) → e^(-λ) * λ^k / k! """
    pass  # TODO

# TODO 4: Graficar las tres distribuciones con los parámetros del proyecto

if __name__ == "__main__":
    print("=== UNIDAD 2: MODELOS DE PROBABILIDAD ===\n")
    # TODO: calcular probabilidades con contexto del proyecto
    # Ej: ¿Cuál es la probabilidad de que un estudiante típico
    #     obtenga nota >= 51? (distribución normal de notas)
