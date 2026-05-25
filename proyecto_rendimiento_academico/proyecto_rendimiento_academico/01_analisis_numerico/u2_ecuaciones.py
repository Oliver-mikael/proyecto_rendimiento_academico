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
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# FUNCIÓN OBJETIVO DEL PROYECTO
# (viene de u7_minimos_cuadrados.py — por ahora usamos coeficientes fijos)
# ─────────────────────────────────────────────
def modelo_nota(horas, beta0, beta1, beta2, asistencia_fija):
    return beta0 + beta1 * horas + beta2 * asistencia_fija

def f_objetivo(horas, beta0, beta1, beta2, asistencia_fija, nota_objetivo=51):
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
    fa = f(a, *args)
    fb = f(b, *args)
    if fa * fb >= 0:
        raise ValueError("No hay cambio de intervalo en el intervalo.")
    tabla = []
    c_anterior = a
    for iteracion in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c, *args)
        error = error_aproximacion(c, c_anterior)
        tabla.append([iteracion, a, b, c, fc, error])
        if criterio_parada(c, c_anterior, tolerancia):
            return c, tabla
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        c_anterior = c
    print("Bisección : se alcanzo el máximo de iteraciones")
    return c, tabla
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
    x = x0
    tabla = []
    for iteracion in range(1, max_iter + 1):
        fx = f(x, *args)
        dfx = df(*args)
        if dfx == 0:
            break
        x_nuevo = x - fx / dfx
        error = error_aproximacion(x, x_nuevo)
        tabla.append([iteracion, x, fx, error])
        if criterio_parada(x, x_nuevo, tolerancia):
            return x_nuevo, tabla
        x = x_nuevo
    return x, tabla

# ─────────────────────────────────────────────
# TODO 3: Comparar ambos métodos y graficar
# ─────────────────────────────────────────────
def graficar_convergencia(tabla_biseccion, tabla_newton):
    """
    Grafica el error en cada iteración para ambos métodos.
    Muestra visualmente que Newton converge más rápido.

    Usar matplotlib. Guardar en: ../resultados/graficos/u2_convergencia.png
    """
    iter_b = [fila[0] for fila in tabla_biseccion]
    err_b     = [fila[5] for fila in tabla_biseccion]  # columna 5 en bisección
    
    iter_n = [fila[0] for fila in tabla_newton]
    err_n     = [fila[3] for fila in tabla_newton]  # columna 3 en newton
            
    plt.figure()
    plt.plot(iter_b, err_b, label='Bisección')
    plt.plot(iter_n, err_n, label='Newton')
    plt.xlabel('Iteración')
    plt.ylabel('Error')
    plt.title('Convergencia: Bisección vs Newton')
    plt.legend()
    plt.grid(True)
    plt.savefig('../resultados/graficos/u2_convergencia.png')
    plt.show()
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
    horas_b, tabla_b = biseccion(f_objetivo, 0, 30, args)
    horas_n, tabla_n = newton_raphson(f_objetivo, df_objetivo, 10, args)
    # TODO: llamar a biseccion() con intervalo [0, 30]
    print("\nTABLA BISECCIÓN...")
    for fila in tabla_b:
        print(f"  iter {fila[0]}: c={fila[3]:.4f}  error={fila[5]}")
    # TODO: llamar a newton_raphson() con x0 = 10
    print("\nTABLA NEWTON...")
    for fila in tabla_n:
        print(f"  iter {fila[0]}: c={fila[1]:.4f}  error={fila[3]}")
    # TODO: imprimir tablas de iteraciones
    # TODO: comparar resultados y número de iteraciones
    # TODO: llamar a graficar_convergencia()
    print("\nGRÁFICA DE CONVERGENCIA...")
    grafico = graficar_convergencia(tabla_b, tabla_n)
    print("\nPREGUNTA RESUELTA:")
    print(f"Con {asistencia_fija*100:.0f}% de asistencia,")
    print(f"se necesitan ≈ {horas_b:.2f} horas semanales para aprobar.")
