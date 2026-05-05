# -*- coding: utf-8 -*-
"""
ARCHIVO   : u6_ecuaciones_dif.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 6
TEMA      : Ecuaciones Diferenciales Ordinarias

PROPÓSITO : Modelar cómo evoluciona el rendimiento de un estudiante
            a lo largo del semestre mediante una EDO.

MODELO:
    dR/dt = k * R * (1 - R/100)   ← modelo logístico de aprendizaje
    R(0)  = R0                     ← nota inicial (ej: 30 puntos en semana 0)

    Interpretación:
    - R crece rápido cuando está lejos de 100 (mucho por aprender)
    - R crece lento cuando se acerca a 100 (rendimiento máximo)
    - k controla la velocidad de aprendizaje

MÉTODO:
    Runge-Kutta de 4to orden (RK4)

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# TODO 1: Runge-Kutta 4to orden
# ─────────────────────────────────────────────
def runge_kutta4(f, y0, t0, tf, h):
    """
    Resuelve dy/dt = f(t, y) desde t0 hasta tf con paso h.

    FÓRMULAS:
        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h,   y + h*k3)
        y_nuevo = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

    PASOS:
    1. Inicializar listas ts=[t0], ys=[y0]
    2. Bucle mientras t < tf:
       a. Calcular k1, k2, k3, k4
       b. Calcular y_nuevo
       c. t = t + h
       d. Agregar t e y_nuevo a las listas
    3. Retornar np.array(ts), np.array(ys)
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 2: Modelo de aprendizaje logístico
# ─────────────────────────────────────────────
def modelo_aprendizaje(t, R, k=0.1):
    """
    EDO del rendimiento académico.
    dR/dt = k * R * (1 - R/100)

    Parámetros:
        t : tiempo (semana del semestre)
        R : rendimiento actual (nota 0-100)
        k : velocidad de aprendizaje
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 3: Graficar la predicción
# ─────────────────────────────────────────────
def graficar_prediccion(ts, Rs, nota_aprobado=51):
    """
    Grafica la curva de rendimiento predicha.
    Marcar en qué semana el estudiante cruza la nota de aprobado.
    Guardar en: ../resultados/graficos/u6_rk4_prediccion.png
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 6: RUNGE-KUTTA 4TO ORDEN ===\n")

    # Parámetros del semestre
    t0 = 0    # semana inicial
    tf = 16   # semana final (16 semanas de semestre)
    h  = 0.5  # paso (cada media semana)
    R0 = 30   # nota inicial del estudiante (semana 0)

    # TODO: llamar a runge_kutta4() con modelo_aprendizaje
    # TODO: imprimir tabla semana → rendimiento predicho
    # TODO: graficar
    # TODO: determinar en qué semana el estudiante supera nota 51
