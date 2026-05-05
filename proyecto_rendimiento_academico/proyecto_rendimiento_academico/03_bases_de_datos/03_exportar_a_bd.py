# -*- coding: utf-8 -*-
"""
ARCHIVO   : 03_exportar_a_bd.py
CARPETA   : 03_bases_de_datos/
MATERIA   : Bases de Datos
PROPÓSITO : Leer el CSV generado por 00_simulacion/generar_datos.py
            y cargarlo a la base de datos PostgreSQL.

FLUJO:
    estudiantes.csv  →  este script  →  PostgreSQL

REQUISITO : pip install psycopg2-binary pandas

CONFIGURACIÓN DE CONEXIÓN (modificar con tus datos):
    HOST     = 'localhost'
    PORT     = 5432
    DATABASE = 'proyecto_rendimiento'
    USER     = 'postgres'
    PASSWORD = '[tu contraseña]'

AUTOR     : [Tu nombre]   FECHA: [Fecha]
"""

import pandas as pd
# import psycopg2  # descomentar cuando instales psycopg2

# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────
CONFIG_BD = {
    'host'    : 'localhost',
    'port'    : 5432,
    'database': 'proyecto_rendimiento',
    'user'    : 'postgres',
    'password': 'tu_password'  # TODO: cambiar
}

RUTA_CSV = '../datos/raw/estudiantes.csv'

# ─────────────────────────────────────────────
# TODO 1: Conectar a PostgreSQL
# ─────────────────────────────────────────────
def conectar():
    """
    Retorna una conexión a PostgreSQL usando psycopg2.
    Si falla, lanzar excepción con mensaje claro.
    """
    pass  # TODO

# ─────────────────────────────────────────────
# TODO 2: Insertar estudiantes
# ─────────────────────────────────────────────
def insertar_estudiantes(conn, df):
    """
    Inserta una fila en 'estudiante' por cada registro del DataFrame.
    Usar cursor.executemany() para eficiencia.
    """
    pass  # TODO

# ─────────────────────────────────────────────
# TODO 3: Insertar registros académicos
# ─────────────────────────────────────────────
def insertar_registros(conn, df):
    """
    Inserta una fila en 'registro_academico' por cada estudiante.
    """
    pass  # TODO

# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=== EXPORTAR DATOS A POSTGRESQL ===\n")

    # TODO: leer el CSV
    # TODO: conectar a la BD
    # TODO: insertar datos
    # TODO: imprimir resumen: "X filas insertadas correctamente"
    # TODO: cerrar conexión

    print("\nNOTA: Asegúrate de haber ejecutado primero:")
    print("  1. 00_simulacion/generar_datos.py")
    print("  2. 03_bases_de_datos/01_esquema.sql  (en PostgreSQL)")
