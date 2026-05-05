# -*- coding: utf-8 -*-
"""
ARCHIVO   : u3_sistemas.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 3
TEMA      : Solución de Sistemas de Ecuaciones

PROPÓSITO : Resolver el sistema de ecuaciones normales de la regresión
            múltiple usando Gauss-Seidel.
            La ecuación normal es: (X^T * X) * beta = X^T * y
            donde beta = [beta0, beta1, beta2] son los coeficientes del modelo.

CONEXIÓN:
    Los coeficientes beta que se obtienen aquí se usan en:
    → u2_ecuaciones.py (optimización)
    → u4_interpolacion.py (predicción)
    → u7_minimos_cuadrados.py (ya tiene la regresión completa)

DEPENDENCIAS:
    from u1_errores import criterio_parada

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
from u1_errores import criterio_parada

# ─────────────────────────────────────────────
# TODO 1: Método de Gauss-Seidel
# ─────────────────────────────────────────────
def gauss_seidel(A, b, x0=None, tolerancia=1e-6, max_iter=1000):
    """
    Resuelve el sistema A*x = b por el método de Gauss-Seidel.

    PASOS:
    1. Verificar que la diagonal de A no tenga ceros (división por cero)
    2. Inicializar x = x0 (si None, usar vector de ceros)
    3. Bucle hasta max_iter:
       Para cada i: x[i] = (b[i] - suma_j≠i(A[i,j]*x[j])) / A[i,i]
       Calcular error máximo entre x_nuevo y x_anterior
       Si criterio_parada() → retornar x y número de iteraciones
    4. Advertir si no converge

    NOTA: Gauss-Seidel converge si A es diagonalmente dominante.
    La matriz X^T*X de mínimos cuadrados cumple esa condición.
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 2: Verificar dominancia diagonal
# ─────────────────────────────────────────────
def es_diagonalmente_dominante(A):
    """
    Verifica si la matriz A es diagonalmente dominante.
    Condición: |A[i,i]| > suma(|A[i,j]|) para j ≠ i, para todo i.
    Retorna True/False.
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 3: GAUSS-SEIDEL ===\n")

    # TODO: probar con un sistema 3x3 de ejemplo académico
    # Ejemplo: resolver el sistema de la ecuación normal de regresión
    # con datos pequeños (5 estudiantes) para verificar manualmente.

    # A = [[...]]
    # b = [...]
    # solucion = gauss_seidel(A, b)
    # print(f"Solución: {solucion}")
    # print(f"Verificación A*x = {A @ solucion}")  # debe ser ≈ b
