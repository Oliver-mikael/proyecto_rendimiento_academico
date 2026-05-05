# -*- coding: utf-8 -*-
"""
ARCHIVO   : u6_anova.py
MATERIA   : Estadística II — Unidad 6
TEMA      : Análisis de Varianza (ANOVA de un factor)

HIPÓTESIS DEL PROYECTO:
    Factor: nivel de asistencia (3 niveles: baja / media / alta)
    H0: μ_baja = μ_media = μ_alta  (todas las notas medias son iguales)
    H1: al menos una media es diferente

TABLA ANOVA:
    | Fuente     | SC  | GL  | CM  | F   | p-valor |
    | Entre gpos | SSB | k-1 | MSB | F   |         |
    | Dentro     | SSW | N-k | MSW |     |         |
    | Total      | SST | N-1 |     |     |         |

AUTOR     : [Tu nombre]   FECHA: [Fecha]
"""
import numpy as np

# TODO 1: ANOVA completamente manual
def anova_un_factor(grupos, alpha=0.05):
    """
    grupos: lista de arrays (uno por nivel)
    Calcula: SST, SSB, SSW, MSB, MSW, F, p-valor
    Retorna diccionario con todos los valores de la tabla
    """
    pass  # TODO

# TODO 2: Imprimir tabla ANOVA formateada
def imprimir_tabla_anova(resultado):
    pass  # TODO

if __name__ == "__main__":
    print("=== UNIDAD 6: ANOVA DE UN FACTOR ===\n")
    # TODO: cargar datos desde CSV
    # TODO: separar notas en 3 grupos por nivel de asistencia
    # TODO: aplicar anova_un_factor()
    # TODO: imprimir tabla y conclusión
