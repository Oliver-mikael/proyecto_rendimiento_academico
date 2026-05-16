# -*- coding: utf-8 -*-
"""
ARCHIVO   : generar_datos.py
CARPETA   : 00_simulacion/
MATERIA   : (base de todo el proyecto)
PROPÓSITO : Generar datos sintéticos de estudiantes y guardarlos en CSV.
            Este archivo es el PUNTO DE PARTIDA del proyecto.
            Todos los demás archivos leen desde datos/raw/estudiantes.csv

VARIABLES SIMULADAS:
    - id_estudiante     : identificador único (1 al N)
    - horas_estudio     : horas de estudio por semana (distribución normal)
    - asistencia        : proporción de clases asistidas, 0 a 1 (binomial)
    - nota_parcial1     : nota del primer parcial (0 a 100)
    - nota_parcial2     : nota del segundo parcial (0 a 100)
    - nota_final        : nota final del semestre (0 a 100)
    - grupo_asistencia  : categoría 'baja', 'media', 'alta' (para ANOVA)

RELACIÓN USADA:
    nota_final = 20 + 2*horas_estudio + 30*asistencia + error_aleatorio

AUTOR     : [Tu nombre]
FECHA     : [Fecha]
"""

import numpy as np
import pandas as pd
import os

# ─────────────────────────────────────────────
# PARÁMETROS DE SIMULACIÓN (modifica aquí)
# ─────────────────────────────────────────────
N_ESTUDIANTES = 200   # cantidad de estudiantes a simular
SEMILLA       = 42    # semilla para reproducibilidad (siempre el mismo resultado)
NOTA_APROBADO = 51    # nota mínima para aprobar

# ─────────────────────────────────────────────
# TODO 1: Implementar la función de simulación
# ─────────────────────────────────────────────
def simular_estudiantes(n, semilla):
    """
    Genera n estudiantes con datos simulados.

    PASOS A IMPLEMENTAR:
    1. Fijar la semilla con np.random.seed(semilla)
    2. Generar horas_estudio con distribución normal (media=15, std=5)
       → Limitar entre 0 y 30 con np.clip()
    3. Generar asistencia con distribución binomial (n=20 intentos, p=0.85)
       → Dividir entre 20 para obtener proporción 0..1
    4. Calcular nota_final = 20 + 2*horas + 30*asistencia + error_normal(0,5)
       → Limitar entre 0 y 100
    5. Calcular nota_parcial1 = 0.6*nota_final + ruido
    6. Calcular nota_parcial2 = 0.8*nota_final + ruido
    7. Crear columna grupo_asistencia:
       - asistencia < 0.70  → 'baja'
       - asistencia 0.70-0.85 → 'media'
       - asistencia > 0.85  → 'alta'
    8. Retornar un DataFrame de pandas con todas las columnas
    """
    # Ejemplo simple (NO es el código del proyecto):
            # Paso 1: fijar semilla en simular_estudiantes"
            import numpy as np
            
            np.random.seed(semilla)

            # Paso 2: Generar horas_estudio con distribución normal (media=15, std=5) → Limitar entre 0 y 30 con np.clip()"
            # Ejemplo: edades de personas (NO es el proyecto)
            edades = np.random.normal(loc=30, scale=5, size=50)
            # Algunas pueden salir negativas o muy grandes → limitamos:
            edades = np.clip(horas_estudio, 0, 30)  # mínimo 18, máximo 65

            # Paso 3: Generar asistencia con distribución binomial (n=20 intentos, p=0.85) → Dividir entre 20 para obtener proporción 0..1"
            # Ejemplo: de 10 preguntas con 70% de chance de acertar
            respuestas = np.random.binomial(n=20, p=0.85, size=n)
            # → algo como [7, 8, 6, 9, 7]  (respuestas correctas por persona)
            proporcion = respuestas / 20   # → [0.7, 0.8, 0.6, 0.9, 0.7]
# ─────────────────────────────────────────────
# TODO 2: Guardar el CSV
# ─────────────────────────────────────────────
def guardar_csv(df, ruta):
    """
    Guarda el DataFrame en un archivo CSV.

    PASOS:
    1. Crear la carpeta si no existe (os.makedirs)
    2. Guardar con df.to_csv(ruta, index=False)
    3. Imprimir confirmación con la ruta y el número de filas
    """
    pass  # TODO: reemplazar con la implementación


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== SIMULACIÓN DE DATOS ===\n")

    # TODO 3: Llamar a simular_estudiantes() y guardar el resultado
    # Ruta destino: ../datos/raw/estudiantes.csv

    # TODO 4: Imprimir las primeras 5 filas con df.head()

    # TODO 5: Imprimir estadísticos básicos con df.describe()

    print("\nArchivo generado correctamente.")
