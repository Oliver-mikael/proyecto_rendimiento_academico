# -*- coding: utf-8 -*-
"""
ARCHIVO   : u4_estimacion.py
MATERIA   : Estadística II — Unidad 4
TEMA      : Estimación Puntual e Intervalos de Confianza

PROPÓSITO : Estimar la nota media real de todos los estudiantes
            con un intervalo de confianza del 95%.

PREGUNTA  : Con nuestra muestra de 200 estudiantes, ¿entre qué valores
            podemos decir con 95% de confianza que está la nota promedio
            de TODOS los estudiantes de la carrera?

AUTOR     : [Tu nombre]   FECHA: [Fecha]
"""
import numpy as np

# TODO 1: Intervalo de confianza para la media (t de Student)
def intervalo_confianza_t(muestra, confianza=0.95):
    """
    IC = x_barra ± t_(α/2, n-1) * (s / sqrt(n))
    Retorna: (limite_inf, limite_sup, margen_error)
    """
    pass  # TODO

# TODO 2: Tamaño de muestra necesario dado un margen de error
def tamano_muestra_necesario(margen_error, desv_std_estimada, confianza=0.95):
    """
    n = (z_(α/2) * sigma / E)²
    """
    pass  # TODO

if __name__ == "__main__":
    print("=== UNIDAD 4: ESTIMACIÓN E INTERVALOS DE CONFIANZA ===\n")
    # TODO: cargar notas desde CSV
    # TODO: calcular IC 95% y IC 99%
    # TODO: interpretar en lenguaje simple
