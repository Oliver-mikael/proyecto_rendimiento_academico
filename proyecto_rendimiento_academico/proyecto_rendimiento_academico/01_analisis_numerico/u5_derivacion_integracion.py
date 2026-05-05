# -*- coding: utf-8 -*-
"""
ARCHIVO   : u5_derivacion_integracion.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 5
TEMA      : Derivación e Integración Numérica

PROPÓSITO :
    DERIVACIÓN → calcular qué tan rápido mejora el rendimiento de un
                 estudiante por cada hora adicional de estudio.
    INTEGRACIÓN → calcular el total de horas de estudio acumuladas
                  durante el semestre.

MÉTODOS:
    Derivación  : diferencias hacia adelante, hacia atrás y centradas
    Integración : Regla del Trapecio y Regla de Simpson compuesta

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# DERIVACIÓN NUMÉRICA
# ─────────────────────────────────────────────

# TODO 1: Diferencia hacia adelante
def diff_adelante(f, x, h=1e-4):
    """ f'(x) ≈ (f(x+h) - f(x)) / h """
    pass  # TODO

# TODO 2: Diferencia hacia atrás
def diff_atras(f, x, h=1e-4):
    """ f'(x) ≈ (f(x) - f(x-h)) / h """
    pass  # TODO

# TODO 3: Diferencia centrada (más precisa)
def diff_centrada(f, x, h=1e-4):
    """ f'(x) ≈ (f(x+h) - f(x-h)) / (2h) """
    pass  # TODO

# TODO 4: Comparar los tres métodos y sus errores


# ─────────────────────────────────────────────
# INTEGRACIÓN NUMÉRICA
# ─────────────────────────────────────────────

# TODO 5: Regla del Trapecio compuesta
def trapecio(f, a, b, n):
    """
    Integral de f en [a,b] con n subintervalos.
    Fórmula: h/2 * (f(x0) + 2*f(x1) + ... + 2*f(xn-1) + f(xn))
    """
    pass  # TODO

# TODO 6: Regla de Simpson compuesta
def simpson(f, a, b, n):
    """
    Integral de f en [a,b] con n subintervalos (n debe ser par).
    Fórmula: h/3 * (f(x0) + 4*f(x1) + 2*f(x2) + ... + 4*f(xn-1) + f(xn))
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 5: DERIVACIÓN E INTEGRACIÓN NUMÉRICA ===\n")

    # Función de horas de estudio por semana (curva típica de un semestre)
    def horas_por_semana(t):
        return 5 + 2 * np.sin(t)  # sube hacia los exámenes

    # TODO: calcular derivada en t=8 (mitad del semestre) con los 3 métodos
    # TODO: calcular horas totales (integral de 0 a 16 semanas)
    # TODO: comparar Trapecio vs Simpson con diferentes n
    # TODO: graficar la función y el área bajo la curva
