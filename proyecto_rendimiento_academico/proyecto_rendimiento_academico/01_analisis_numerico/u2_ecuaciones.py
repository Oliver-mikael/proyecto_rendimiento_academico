# -*- coding: utf-8 -*-
"""
ARCHIVO   : u2_ecuaciones.py
CARPETA   : 01_analisis_numerico/
MATERIA   : Análisis Numérico — Unidad 2
TEMA      : Resolución de Ecuaciones Algebraicas y Trascendentes

PROPÓSITO : Implementar bisección y Newton-Raphson para encontrar
            las horas mínimas de estudio necesarias para aprobar.

PREGUNTA DEL PROYECTO:
    ¿Cuántas horas semanales mínimas necesita estudiar un estudiante
    con X% de asistencia para alcanzar la nota de aprobado (51)?

    Esto es: resolver f(horas) = modelo(horas) - 51 = 0

MÉTODOS:
    - Bisección       : divide el intervalo a la mitad en cada paso
    - Newton-Raphson  : usa la derivada para converger más rápido

DEPENDENCIAS:
    from u1_errores import error_aproximacion, criterio_parada

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
from u1_errores import error_aproximacion, criterio_parada

# ─────────────────────────────────────────────
# FUNCIÓN OBJETIVO DEL PROYECTO
# (viene de u7_minimos_cuadrados.py — por ahora usamos coeficientes fijos)
# ─────────────────────────────────────────────
def modelo_nota(horas, beta0, beta1, beta2, asistencia_fija):
    """
    Modelo lineal de predicción de nota.
    nota = beta0 + beta1*horas + beta2*asistencia_fija

    beta0, beta1, beta2 vendrán de la regresión (u7_minimos_cuadrados.py)
    Por ahora usar valores de prueba: beta0=21, beta1=2, beta2=30
    """
    return beta0 + beta1 * horas + beta2 * asistencia_fija


def f_objetivo(horas, beta0, beta1, beta2, asistencia_fija, nota_objetivo=51):
    """
    Función cuya raíz queremos encontrar.
    f(horas) = modelo_nota(horas) - nota_objetivo

    Cuando f(horas) = 0 → encontramos las horas exactas para aprobar.
    """
    return modelo_nota(horas, beta0, beta1, beta2, asistencia_fija) - nota_objetivo


def df_objetivo(beta1):
    """
    Derivada de f_objetivo respecto a horas.
    Como el modelo es lineal: df/dhoras = beta1 (constante)
    """
    return beta1


# ─────────────────────────────────────────────
# TODO 1: Método de Bisección
# ─────────────────────────────────────────────
def biseccion(f, a, b, args, tolerancia=1e-5, max_iter=100):
    """
    Encuentra la raíz de f(x, *args) en el intervalo [a, b].

    PASOS A IMPLEMENTAR:
    1. Verificar que f(a)*f(b) < 0 (cambio de signo — condición de Bolzano)
       Si no hay cambio de signo, lanzar ValueError con mensaje claro.
    2. Inicializar tabla de iteraciones: [iteracion, a, b, c, f(c), error]
    3. Bucle hasta max_iter:
       a. c = (a + b) / 2
       b. Calcular f(c)
       c. Calcular error con error_aproximacion() (usa c y el c anterior)
       d. Guardar fila en la tabla
       e. Si criterio_parada() → retornar c y la tabla
       f. Si f(a)*f(c) < 0 → b = c, sino a = c
    4. Retornar (c, tabla_iteraciones)

    La tabla de iteraciones es IMPORTANTE para mostrar en el informe.
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 2: Método de Newton-Raphson
# ─────────────────────────────────────────────
def newton_raphson(f, df, x0, args, tolerancia=1e-5, max_iter=100):
    """
    Encuentra la raíz de f(x, *args) partiendo de x0.
    Fórmula: x_nuevo = x - f(x) / f'(x)

    PASOS A IMPLEMENTAR:
    1. Inicializar x = x0
    2. Inicializar tabla de iteraciones: [iteracion, x, f(x), error]
    3. Bucle hasta max_iter:
       a. Calcular f(x) y f'(x)
       b. Si f'(x) ≈ 0 → detener (división por cero)
       c. x_nuevo = x - f(x) / f'(x)
       d. Calcular error con error_aproximacion()
       e. Guardar fila en la tabla
       f. Si criterio_parada() → retornar x_nuevo y la tabla
       g. x = x_nuevo
    4. Retornar (x, tabla_iteraciones)
    """
    pass  # TODO


# ─────────────────────────────────────────────
# TODO 3: Comparar ambos métodos y graficar
# ─────────────────────────────────────────────
def graficar_convergencia(tabla_biseccion, tabla_newton):
    """
    Grafica el error en cada iteración para ambos métodos.
    Muestra visualmente que Newton converge más rápido.

    Usar matplotlib. Guardar en: ../resultados/graficos/u2_convergencia.png
    """
    pass  # TODO


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== UNIDAD 2: BISECCIÓN Y NEWTON-RAPHSON ===\n")

    # Coeficientes del modelo (valores de prueba — vendrán de u7 después)
    beta0, beta1, beta2 = 21.0, 2.0, 30.0
    asistencia_fija = 0.80   # 80% de asistencia
    nota_objetivo   = 51     # nota mínima para aprobar

    args = (beta0, beta1, beta2, asistencia_fija, nota_objetivo)

    # TODO: llamar a biseccion() con intervalo [0, 30]
    # TODO: llamar a newton_raphson() con x0 = 10
    # TODO: imprimir tablas de iteraciones
    # TODO: comparar resultados y número de iteraciones
    # TODO: llamar a graficar_convergencia()

    print("\nPREGUNTA RESUELTA:")
    print(f"Con {asistencia_fija*100:.0f}% de asistencia,")
    print(f"se necesitan ≈ X horas semanales para aprobar con nota {nota_objetivo}.")
