-- ═══════════════════════════════════════════════════════════════
-- ARCHIVO  : 04_consultas.sql
-- MATERIA  : Bases de Datos
-- PROPÓSITO: Consultas SQL de análisis sobre los datos del proyecto.
-- ═══════════════════════════════════════════════════════════════

-- ─────────────────────────────────────────────
-- CONSULTAS BÁSICAS (SELECT, WHERE, ORDER BY)
-- ─────────────────────────────────────────────

-- TODO 1: Listar todos los estudiantes con nota final mayor a 51
-- (los que aprobaron)


-- TODO 2: Listar los 10 estudiantes con mayor nota final


-- TODO 3: Listar estudiantes con asistencia baja que aprobaron
-- (casos interesantes para analizar)


-- ─────────────────────────────────────────────
-- CONSULTAS DE AGREGACIÓN (GROUP BY, HAVING)
-- ─────────────────────────────────────────────

-- TODO 4: Promedio de nota final por grupo de asistencia
-- Resultado esperado:
-- grupo_asistencia | promedio_nota | cantidad_estudiantes
-- baja             | 55.2          | 28
-- media            | 68.7          | 89
-- alta             | 78.4          | 83


-- TODO 5: Promedio de horas de estudio de los estudiantes que aprobaron
-- vs los que reprobaron


-- TODO 6: Distribución de notas por rangos (0-50, 51-70, 71-90, 91-100)
-- Usar CASE WHEN


-- ─────────────────────────────────────────────
-- CONSULTAS DE UNIÓN (JOIN)
-- ─────────────────────────────────────────────

-- TODO 7: Unir estudiante con registro_academico para mostrar
-- nombre + nota_final + grupo_asistencia


-- ─────────────────────────────────────────────
-- CONSULTAS PARA EL PROYECTO (conectan con Python y estadística)
-- ─────────────────────────────────────────────

-- TODO 8: Calcular correlación entre horas_estudio y nota_final en SQL
-- PostgreSQL tiene la función corr(X, Y)


-- TODO 9: Vista que resume el rendimiento por grupo
-- CREATE VIEW resumen_rendimiento AS ...
