# Carpeta: datos/

## Estructura

```
datos/
├── raw/
│   └── estudiantes.csv     ← generado por 00_simulacion/generar_datos.py
│                              NO editar a mano
└── procesados/
    └── (vacío por ahora)   ← aquí irán datos filtrados o transformados
```

## Columnas de estudiantes.csv

| Columna | Tipo | Descripción |
|---------|------|-------------|
| id_estudiante | entero | identificador único (1 al N) |
| horas_estudio | decimal | horas de estudio por semana |
| asistencia | decimal | proporción de clases asistidas (0 a 1) |
| nota_parcial1 | decimal | nota del primer parcial (0-100) |
| nota_parcial2 | decimal | nota del segundo parcial (0-100) |
| nota_final | decimal | nota final del semestre (0-100) |
| grupo_asistencia | texto | 'baja', 'media' o 'alta' |

## Cómo regenerar los datos

```bash
cd 00_simulacion
python generar_datos.py
```

El archivo se guarda automáticamente en `datos/raw/estudiantes.csv`.
