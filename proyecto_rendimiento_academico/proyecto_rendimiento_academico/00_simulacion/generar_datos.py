# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os

N_ESTUDIANTES = 200
SEMILLA       = 42
NOTA_APROBADO = 51

def simular_estudiantes(n, semilla):
    """Genera n estudiantes con datos simulados."""
    # Paso 1: semilla
    np.random.seed(semilla)
    # Paso 2: horas de estudio
    horas_estudio = np.random.normal(loc=15, scale=5, size=n)
    horas_estudio = np.clip(horas_estudio, 0, 30)
    # Paso 3: asistencia
    asistencia = np.random.binomial(n=20, p=0.85, size=n) / 20
    # Paso 4: nota final
    nota_final = 20 + 2*horas_estudio + 30*asistencia + np.random.normal(loc=0, scale=5, size=n)
    nota_final = np.clip(nota_final, 0, 100)
    # Paso 5: parcial 1
    nota_parcial1 = 0.6 * nota_final + np.random.normal(loc=0, scale=5, size=n)
    nota_parcial1 = np.clip(nota_parcial1, 0, 100)
    # Paso 6: parcial 2
    nota_parcial2 = 0.8 * nota_final + np.random.normal(loc=0, scale=4, size=n)
    nota_parcial2 = np.clip(nota_parcial2, 0, 100)
    # Paso 7: grupo asistencia
    grupo_asistencia = np.where(asistencia < 0.70, 'baja',
                       np.where(asistencia <= 0.85, 'media', 'alta'))
    # Paso 8: DataFrame
    df = pd.DataFrame({
        'id_estudiante'   : np.arange(1, n+1),
        'horas_estudio'   : horas_estudio,
        'asistencia'      : asistencia,
        'nota_parcial1'   : nota_parcial1,
        'nota_parcial2'   : nota_parcial2,
        'nota_final'      : nota_final,
        'grupo_asistencia': grupo_asistencia,
    })
    return df

def guardar_csv(df, ruta):
    """Guarda el DataFrame en CSV."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df.to_csv(ruta, index=False)
    print(f"Archivo guardado: {ruta} ({len(df)} filas)")

if __name__ == "__main__":
    print("=== SIMULACIÓN DE DATOS ===\n")
    df = simular_estudiantes(N_ESTUDIANTES, SEMILLA)
    guardar_csv(df, 'datos/raw/estudiantes.csv')
    print(df.head())
    print()
    print(df.describe().round(2))
    print("\nArchivo generado correctamente.")
