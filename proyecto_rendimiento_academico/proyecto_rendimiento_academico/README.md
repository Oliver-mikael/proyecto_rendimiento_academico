# Proyecto Integrador — Rendimiento Académico Estudiantil
**Materias:** Análisis Numérico | Estadística II | Bases de Datos  
**Carrera:** Ingeniería de Sistemas — UPEA (4to semestre)  
**Título:** Evaluación del rendimiento académico estudiantil mediante indicadores numéricos  

---

## Capacidades del sistema
- **SIMULAR** → genera datos realistas de estudiantes
- **OPTIMIZAR** → encuentra el mínimo esfuerzo para aprobar
- **PREDECIR** → proyecta el rendimiento futuro

---

## Estructura del proyecto

```
proyecto_rendimiento_academico/
│
├── README.md                          ← este archivo
│
├── 00_simulacion/
│   └── generar_datos.py               ← PASO 1: genera los datos base (CSV)
│
├── 01_analisis_numerico/
│   ├── u1_errores.py                  ← Unidad 1: teoría de errores
│   ├── u2_ecuaciones.py               ← Unidad 2: bisección y Newton-Raphson
│   ├── u3_sistemas.py                 ← Unidad 3: Gauss-Seidel
│   ├── u4_interpolacion.py            ← Unidad 4: interpolación de Lagrange
│   ├── u5_derivacion_integracion.py   ← Unidad 5: derivación e integración numérica
│   ├── u6_ecuaciones_dif.py           ← Unidad 6: Runge-Kutta 4to orden
│   └── u7_minimos_cuadrados.py        ← Unidad 7: regresión múltiple
│
├── 02_estadistica2/
│   ├── u1_variable_aleatoria.py       ← Unidad 1: variables aleatorias
│   ├── u2_modelos_probabilidad.py     ← Unidad 2: distribuciones (normal, Poisson, etc.)
│   ├── u3_dist_muestrales.py          ← Unidad 3: distribuciones muestrales
│   ├── u4_estimacion.py               ← Unidad 4: estimación e intervalos de confianza
│   ├── u5_prueba_hipotesis.py         ← Unidad 5: prueba t de Student
│   └── u6_anova.py                    ← Unidad 6: ANOVA de un factor
│
├── 03_bases_de_datos/
│   ├── 01_esquema.sql                 ← CREATE TABLE (diseño ER)
│   ├── 02_insertar_datos.sql          ← INSERT de los datos simulados
│   ├── 03_exportar_a_bd.py            ← script Python que llena la BD desde CSV
│   └── 04_consultas.sql               ← consultas SQL de análisis
│
├── datos/
│   ├── raw/
│   │   └── estudiantes.csv            ← generado por 00_simulacion
│   └── procesados/
│       └── (datos limpios aquí)
│
├── resultados/
│   ├── graficos/                      ← imágenes .png generadas por matplotlib
│   └── reportes/                      ← salidas .txt con resultados numéricos
│
└── informe/
    └── informe_final.md               ← informe integrador para los profesores
```

---

## Orden de ejecución
1. `00_simulacion/generar_datos.py`       → genera el CSV con datos
2. `03_bases_de_datos/03_exportar_a_bd.py` → carga datos a PostgreSQL
3. `01_analisis_numerico/u1_errores.py`   → primer método numérico
4. (continúa unidad por unidad)
5. `02_estadistica2/u1_variable_aleatoria.py` → análisis estadístico

---

## Estado del proyecto
| Archivo | Estado |
|---------|--------|
| generar_datos.py | TODO |
| u1_errores.py | TODO |
| u2_ecuaciones.py | TODO |
| u3_sistemas.py | TODO |
| u4_interpolacion.py | TODO |
| u5_derivacion_integracion.py | TODO |
| u6_ecuaciones_dif.py | TODO |
| u7_minimos_cuadrados.py | TODO |
| u1_variable_aleatoria.py | TODO |
| u2_modelos_probabilidad.py | TODO |
| u3_dist_muestrales.py | TODO |
| u4_estimacion.py | TODO |
| u5_prueba_hipotesis.py | TODO |
| u6_anova.py | TODO |
| 01_esquema.sql | TODO |
| 02_insertar_datos.sql | TODO |
| 04_consultas.sql | TODO |
