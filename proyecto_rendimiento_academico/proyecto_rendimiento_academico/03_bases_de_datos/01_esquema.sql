-- ═══════════════════════════════════════════════════════════════
-- ARCHIVO  : 01_esquema.sql
-- CARPETA  : 03_bases_de_datos/
-- MATERIA  : Bases de Datos
-- MOTOR    : PostgreSQL
-- PROPÓSITO: Crear el esquema de la base de datos del proyecto.
--            Diseño basado en el Diagrama Entidad-Relación.
-- ═══════════════════════════════════════════════════════════════

-- ─────────────────────────────────────────────
-- ENTIDADES (Tablas principales)
-- ─────────────────────────────────────────────

-- TODO 1: Tabla ESTUDIANTE
-- Atributos: id_estudiante (PK), nombre, semestre, carrera
CREATE TABLE estudiante (
    -- TODO: definir columnas con tipos de datos correctos
    -- Recordar: PK con SERIAL o INTEGER, NOT NULL donde aplique
);

-- TODO 2: Tabla REGISTRO_ACADEMICO
-- Atributos: id_registro (PK), id_estudiante (FK), horas_estudio,
--            asistencia, nota_parcial1, nota_parcial2, nota_final,
--            grupo_asistencia, semestre_academico
CREATE TABLE registro_academico (
    -- TODO: definir columnas
    -- FK: id_estudiante REFERENCES estudiante(id_estudiante)
    -- CHECK: nota_final BETWEEN 0 AND 100
);

-- TODO 3: Tabla GRUPO_ASISTENCIA (tabla de referencia para normalización)
-- Atributos: id_grupo (PK), nombre ('baja','media','alta'), rango_min, rango_max
CREATE TABLE grupo_asistencia (
    -- TODO: definir columnas
);

-- ─────────────────────────────────────────────
-- RELACIONES (cardinalidad)
-- ─────────────────────────────────────────────
-- estudiante (1) ──── (N) registro_academico
--   Un estudiante puede tener múltiples registros (uno por semestre)
--
-- grupo_asistencia (1) ──── (N) registro_academico
--   Cada registro pertenece a un grupo de asistencia

-- ─────────────────────────────────────────────
-- ÍNDICES (para consultas más rápidas)
-- ─────────────────────────────────────────────
-- TODO 4: Crear índice en id_estudiante de registro_academico
-- CREATE INDEX idx_estudiante ON registro_academico(id_estudiante);

-- TODO 5: Crear índice en grupo_asistencia
-- CREATE INDEX idx_grupo ON registro_academico(grupo_asistencia);
