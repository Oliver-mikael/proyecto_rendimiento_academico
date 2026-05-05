# -*- coding: utf-8 -*-
"""
ARCHIVO   : u5_prueba_hipotesis.py
MATERIA   : Estadística II — Unidad 5
TEMA      : Prueba de Hipótesis

HIPÓTESIS DEL PROYECTO:
    H0: La asistencia NO afecta la nota final
        (μ_alta_asistencia = μ_baja_asistencia)
    H1: La alta asistencia SÍ mejora la nota final
        (μ_alta_asistencia > μ_baja_asistencia)

MÉTODO: Prueba t de Student para dos muestras independientes

AUTOR     : [Tu nombre]   FECHA: [Fecha]
"""
import numpy as np

# TODO 1: Prueba t para dos muestras independientes
def prueba_t_dos_muestras(muestra1, muestra2, alpha=0.05, cola='bilateral'):
    """
    Calcula estadístico t y toma decisión.
    cola: 'bilateral', 'derecha', 'izquierda'
    Retorna: (t_calculado, t_critico, p_valor, decision)
    """
    pass  # TODO

# TODO 2: Imprimir resumen de la prueba
def imprimir_resumen_prueba(t_calc, t_crit, p_val, decision, alpha):
    """
    Formato:
    H0: ...   H1: ...
    t calculado: X.XX   t crítico: X.XX
    p-valor: X.XXXX
    α = 0.05
    Decisión: [Rechazar / No rechazar] H0
    Conclusión: [en lenguaje simple]
    """
    pass  # TODO

if __name__ == "__main__":
    print("=== UNIDAD 5: PRUEBA DE HIPÓTESIS ===\n")
    # TODO: cargar datos desde CSV
    # TODO: separar notas por grupo de asistencia alta vs baja
    # TODO: aplicar prueba_t_dos_muestras()
    # TODO: interpretar resultado en el contexto del proyecto
