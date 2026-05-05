# -*- coding: utf-8 -*-
"""
ARCHIVO   : u4_interpolacion.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 4  ← TEMA DE HOY EN CLASE
TEMA      : Interpolación

PROPÓSITO : Estimar la nota de un estudiante en momentos intermedios
            del semestre usando los parciales conocidos.

PREGUNTA DEL PROYECTO:
    Si un estudiante tuvo nota 62 en el parcial 1 (semana 4)
    y nota 74 en el parcial 2 (semana 8), ¿cuál sería su nota
    aproximada en la semana 6?

MÉTODOS:
    - Interpolación de Lagrange (principal)
    - Diferencias divididas de Newton (complementario)

DATOS DE ENTRADA:
    x_puntos = [semana del parcial 1, semana del parcial 2, semana del final]
    y_puntos = [nota_parcial1, nota_parcial2, nota_final]

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# TODO 1: Interpolación de Lagrange
# ─────────────────────────────────────────────
def lagrange(x_puntos, y_puntos, x):
    """
    Evalúa el polinomio de Lagrange en el punto x.

    FÓRMULA:
    P(x) = suma_i [ y_i * producto_j≠i( (x - x_j)/(x_i - x_j) ) ]

    PASOS:
    1. n = número de puntos
    2. Para cada i:
       a. termino = y_puntos[i]
       b. Para cada j ≠ i:
          termino *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
       c. sumar termino al resultado
    3. Retornar resultado

    Ejemplo:
        x_puntos = [4, 8, 16]   (semanas de evaluación)
        y_puntos = [62, 74, 83] (notas en esas semanas)
        lagrange(x_puntos, y_puntos, 6) → nota estimada en semana 6
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 2: Graficar el polinomio interpolante
# ─────────────────────────────────────────────
def graficar_interpolacion(x_puntos, y_puntos, x_eval):
    """
    Grafica:
    - Los puntos conocidos (parciales del estudiante)
    - El polinomio de Lagrange continuo
    - El punto interpolado (marcado especialmente)

    Guardar en: ../resultados/graficos/u4_interpolacion.png
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 4: INTERPOLACIÓN DE LAGRANGE ===\n")

    # Datos de un estudiante ejemplo
    semanas = [4, 8, 16]          # semana del parcial 1, parcial 2, final
    notas   = [62.0, 74.0, 83.0]  # notas en esas semanas

    # TODO: calcular nota estimada en semanas intermedias
    # semanas_consulta = [6, 10, 12]
    # para cada semana_consulta: imprimir nota estimada con Lagrange

    # TODO: graficar el polinomio completo
