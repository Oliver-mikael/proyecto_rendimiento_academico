# -*- coding: utf-8 -*-
"""
ARCHIVO   : u7_minimos_cuadrados.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 7
TEMA      : Ajuste de Curvas por Mínimos Cuadrados

PROPÓSITO : Encontrar el modelo que MEJOR ajusta la relación entre
            horas de estudio, asistencia y nota final.

MODELO:
    nota_final = beta0 + beta1*horas + beta2*asistencia + error

    Se resuelve la ecuación normal:
    (X^T * X) * beta = X^T * y
    usando Gauss-Seidel (de u3_sistemas.py)

SALIDA:
    - Coeficientes beta0, beta1, beta2
    - R² (coeficiente de determinación)
    - Gráfico de valores reales vs predichos

DEPENDENCIAS:
    from u3_sistemas import gauss_seidel
    Lee datos desde: ../datos/raw/estudiantes.csv

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from u3_sistemas import gauss_seidel

# ─────────────────────────────────────────────
# TODO 1: Construir la matriz de diseño X
# ─────────────────────────────────────────────
def construir_matriz_disenio(horas, asistencia):
    """
    Construye la matriz X de tamaño (n, 3):
    columna 0 → unos (para el intercepto beta0)
    columna 1 → horas_estudio
    columna 2 → asistencia

    Usar np.column_stack()
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 2: Ecuación normal y solución con Gauss-Seidel
# ─────────────────────────────────────────────
def regresion_minimos_cuadrados(X, y):
    """
    Resuelve (X^T X) beta = X^T y con Gauss-Seidel.
    Retorna el vector beta = [beta0, beta1, beta2]

    PASOS:
    1. XTX = X.T @ X   (producto matricial)
    2. XTy = X.T @ y
    3. beta = gauss_seidel(XTX, XTy)
    4. Retornar beta
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 3: Calcular R² (bondad del ajuste)
# ─────────────────────────────────────────────
def calcular_r2(y_real, y_predicho):
    """
    R² = 1 - SS_res / SS_tot
    SS_res = suma((y_real - y_predicho)²)
    SS_tot = suma((y_real - media(y_real))²)

    Interpretación: R²=1 → ajuste perfecto, R²=0 → sin ajuste
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 4: Graficar reales vs predichos
# ─────────────────────────────────────────────
def graficar_ajuste(y_real, y_predicho):
    """
    Scatter plot de y_real (eje X) vs y_predicho (eje Y).
    La línea diagonal perfecta y=x indica buen ajuste.
    Guardar en: ../resultados/graficos/u7_ajuste_regresion.png
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 7: MÍNIMOS CUADRADOS — REGRESIÓN MÚLTIPLE ===\n")

    # TODO: leer datos desde ../datos/raw/estudiantes.csv
    # TODO: construir matriz X con construir_matriz_disenio()
    # TODO: obtener beta con regresion_minimos_cuadrados()
    # TODO: calcular y_predicho = X @ beta
    # TODO: calcular R² con calcular_r2()
    # TODO: imprimir el modelo obtenido
    # TODO: graficar ajuste

    # Resultado esperado (algo similar a):
    # Modelo: nota = 21.25 + 1.99*horas + 29.86*asistencia
    # R² = 0.87 → el modelo explica el 87% de la variación en las notas
