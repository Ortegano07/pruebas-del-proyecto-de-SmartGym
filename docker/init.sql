-- ============================================
-- MÓDULO SEGURIDAD - AUTENTICACIÓN Y ROLES
-- ============================================

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    rol_id INTEGER NOT NULL REFERENCES roles(id),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================
-- MÓDULO CLIENTES
-- ============================================

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id),
    cedula VARCHAR(20) UNIQUE NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro TIMESTAMP DEFAULT NOW()
);

-- ============================================
-- MÓDULO ENTRENADORES
-- ============================================

CREATE TABLE entrenadores (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id),
    especialidad VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE
);

-- ============================================
-- MÓDULO DEPORTIVO - DISCIPLINAS Y CLASES
-- ============================================

CREATE TABLE disciplinas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT
);

CREATE TABLE sesiones_programadas (
    id SERIAL PRIMARY KEY,
    disciplina_id INTEGER NOT NULL REFERENCES disciplinas(id),
    entrenador_id INTEGER NOT NULL REFERENCES entrenadores(id),
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    cupo_maximo INTEGER NOT NULL CHECK (cupo_maximo > 0),
    cupos_ocupados INTEGER DEFAULT 0 CHECK (cupos_ocupados >= 0),
    activa BOOLEAN DEFAULT TRUE,
    -- Regla de negocio: hora_inicio < hora_fin
    CONSTRAINT chk_horario CHECK (hora_inicio < hora_fin)
);

-- ============================================
-- MÓDULO RESERVAS
-- ============================================

CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    sesion_id INTEGER NOT NULL REFERENCES sesiones_programadas(id),
    fecha_reserva TIMESTAMP DEFAULT NOW(),
    asistio BOOLEAN DEFAULT FALSE,
    -- Restricción: un cliente no puede reservar la misma sesión dos veces
    CONSTRAINT uq_cliente_sesion UNIQUE (cliente_id, sesion_id)
);

-- ============================================
-- MÓDULO CONTROL DE ACCESO (Torniquete)
-- ============================================

CREATE TABLE control_accesos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    fecha_hora_entrada TIMESTAMP DEFAULT NOW(),
    acceso_permitido BOOLEAN DEFAULT TRUE,
    observaciones VARCHAR(255)
);

-- ============================================
-- MÓDULO FINANZAS - PLANES Y MEMBRESÍAS
-- ============================================

CREATE TABLE planes_suscripcion (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT,
    costo DECIMAL(10,2) NOT NULL CHECK (costo > 0),
    duracion_dias INTEGER NOT NULL CHECK (duracion_dias > 0),
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE membresias (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    plan_id INTEGER NOT NULL REFERENCES planes_suscripcion(id),
    fecha_inicio DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Activa'
        CHECK (estado IN ('Activa', 'Por Vencer', 'Vencida', 'Cancelada')),
    -- Regla de negocio: fecha_inicio < fecha_vencimiento
    CONSTRAINT chk_vigencia CHECK (fecha_inicio < fecha_vencimiento)
);

CREATE TABLE pagos (
    id SERIAL PRIMARY KEY,
    membresia_id INTEGER NOT NULL REFERENCES membresias(id),
    monto DECIMAL(10,2) NOT NULL CHECK (monto > 0),
    fecha_pago TIMESTAMP DEFAULT NOW(),
    metodo_pago VARCHAR(50) NOT NULL,
    referencia_externa VARCHAR(100)
);

-- ============================================
-- MÓDULO INVENTARIO - MÁQUINAS Y MANTENIMIENTO
-- ============================================

CREATE TABLE categorias_maquinas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT
);

CREATE TABLE maquinas (
    id SERIAL PRIMARY KEY,
    categoria_id INTEGER NOT NULL REFERENCES categorias_maquinas(id),
    nombre VARCHAR(100) NOT NULL,
    descripcion_tecnica TEXT,
    estado_operativo VARCHAR(30) NOT NULL DEFAULT 'Activa'
        CHECK (estado_operativo IN ('Activa', 'Fuera de Servicio', 'En Mantenimiento')),
    fecha_adquisicion DATE,
    ultima_revision DATE
);

CREATE TABLE tickets_mantenimiento (
    id SERIAL PRIMARY KEY,
    maquina_id INTEGER NOT NULL REFERENCES maquinas(id),
    fecha_reporte TIMESTAMP DEFAULT NOW(),
    descripcion_falla TEXT NOT NULL,
    fecha_resolucion TIMESTAMP,
    costo_reparacion DECIMAL(10,2),
    estado_ticket VARCHAR(20) NOT NULL DEFAULT 'Abierto'
        CHECK (estado_ticket IN ('Abierto', 'En Proceso', 'Resuelto', 'Cancelado'))
);

-- ============================================
-- MÓDULO TIENDA (POS)
-- ============================================

CREATE TABLE productos_tienda (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
    stock_actual INTEGER NOT NULL DEFAULT 0 CHECK (stock_actual >= 0),
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE ventas_tienda (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id),  -- Permitimos ventas sin cliente (anónimas)
    fecha_venta TIMESTAMP DEFAULT NOW(),
    total DECIMAL(10,2) NOT NULL CHECK (total >= 0),
    metodo_pago VARCHAR(50)
);

CREATE TABLE detalle_ventas (
    id SERIAL PRIMARY KEY,
    venta_id INTEGER NOT NULL REFERENCES ventas_tienda(id) ON DELETE CASCADE,
    producto_id INTEGER NOT NULL REFERENCES productos_tienda(id),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario_aplicado DECIMAL(10,2) NOT NULL CHECK (precio_unitario_aplicado >= 0),
    subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0)
);

-- ============================================
-- MÓDULO BIOMÉTRICO (SEGUIMIENTO DE PROGRESO)
-- ============================================

CREATE TABLE evaluaciones_biometricas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    entrenador_id INTEGER NOT NULL REFERENCES entrenadores(id),
    fecha DATE NOT NULL,
    peso_kg DECIMAL(5,2),
    estatura_cm DECIMAL(5,2),
    porcentaje_grasa DECIMAL(5,2),
    observaciones TEXT
);

-- ============================================
-- ÍNDICES PARA OPTIMIZAR CONSULTAS FRECUENTES
-- ============================================

-- Búsqueda de clientes por cédula (control de acceso)
CREATE INDEX idx_clientes_cedula ON clientes(cedula);

-- Consulta de sesiones por fecha
CREATE INDEX idx_sesiones_fecha ON sesiones_programadas(fecha);

-- Consulta de reservas por cliente (para validar solapamiento)
CREATE INDEX idx_reservas_cliente ON reservas(cliente_id);

-- Búsqueda de membresías activas por cliente
CREATE INDEX idx_membresias_cliente_estado ON membresias(cliente_id, estado);

-- Búsqueda de accesos por fecha
CREATE INDEX idx_accesos_fecha ON control_accesos(fecha_hora_entrada);

-- Búsqueda de tickets por máquina
CREATE INDEX idx_tickets_maquina ON tickets_mantenimiento(maquina_id);

-- ============================================
-- INSERTS INICIALES (datos semilla)
-- ============================================

-- Roles básicos del sistema
INSERT INTO roles (nombre) VALUES
    ('Administrador'),
    ('Finanzas'),
    ('Entrenador'),
    ('Cliente');