# -*- coding: utf-8 -*-
"""
ARCHIVO   : u1_errores.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 1
TEMA      : Introducción y Teoría de Errores

PROPÓSITO : Implementar las funciones de error que serán usadas por TODOS
            los demás métodos numéricos del proyecto.
            Este archivo es la BASE de 01_analisis_numerico/.

CONCEPTOS A IMPLEMENTAR:
    - Error absoluto    : |valor_real - valor_aproximado|
    - Error relativo    : error_absoluto / |valor_real|
    - Error porcentual  : error_relativo * 100
    - Cifras significativas
    - Criterio de parada (tolerancia) para métodos iterativos

CONEXIÓN CON EL PROYECTO:
    u2_ecuaciones.py  → usa calcular_error() para detener bisección y Newton
    u3_sistemas.py    → usa calcular_error() para detener Gauss-Seidel
    u4_interpolacion.py → usa cifras_significativas() para mostrar precisión

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
from math import floor, log10
# ─────────────────────────────────────────────
# TODO 1: Error absoluto
# ─────────────────────────────────────────────
def error_absoluto(valor_real, valor_aprox):
    return abs(valor_real-valor_aprox)
# ─────────────────────────────────────────────
# TODO 2: Error relativo
# ─────────────────────────────────────────────
def error_relativo(valor_real, valor_aprox):
    if valor_real == 0:
        return None
    return error_absoluto(valor_real, valor_aprox) / abs(valor_real) 
# ─────────────────────────────────────────────
# TODO 3: Error porcentual
# ─────────────────────────────────────────────
def error_porcentual(valor_real, valor_aprox):
    er = error_relativo(valor_real, valor_aprox)
    if er is None:
       return None
    return er * 100
# ─────────────────────────────────────────────
# TODO 4: Error de aproximación sucesiva
# (para métodos iterativos donde no conocemos el valor real)
# ─────────────────────────────────────────────
def error_aproximacion(x_nuevo, x_anterior):
    if x_nuevo == 0:
        return None
    return abs(x_nuevo - x_anterior)/ abs(x_nuevo)
# ─────────────────────────────────────────────
# TODO 5: Verificar criterio de parada
# ─────────────────────────────────────────────
def criterio_parada(x_nuevo, x_anterior, tolerancia):
    return error_aproximacion(x_nuevo, x_anterior) < tolerancia
# ─────────────────────────────────────────────
# TODO 6: Cifras significativas
# ─────────────────────────────────────────────
def cifras_significativas(valor, n):
    if valor == 0:
        return 0
    return round(valor, n - 1 - int(floor(log10(abs(valor)))))
# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL — Prueba de las funciones
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 1: TEORÍA DE ERRORES ===\n")

    # TODO 7: Probar cada función con ejemplos del rendimiento académico
    # Ejemplo: valor_real = nota obtenida por el modelo
    #          valor_aprox = nota real del estudiante

    valor_real  = 78.5   # nota real del estudiante
    valor_aprox = 75.2   # nota predicha por el modelo

    # TODO: llamar a cada función e imprimir resultados con f-strings
    # Formato sugerido:
    # print(f"Error absoluto   : {error_absoluto(valor_real, valor_aprox):.4f}")
    # print(f"Error relativo   : {error_relativo(valor_real, valor_aprox):.6f}")
    # print(f"Error porcentual : {error_porcentual(valor_real, valor_aprox):.4f} %")

    print("\n[Prueba de criterio de parada]")
    # TODO: simular 5 iteraciones de un método y mostrar cómo converge el error
