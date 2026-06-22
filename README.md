# ReadExcelExample
Sistema backend en **FastAPI + PostgreSQL + SQLAlchemy** para gestionar trabajadores, roles, permisos y cálculo de pagos.  
Incluye autenticación con **JWT** y contraseñas encriptadas con **bcrypt**.

---

## 🚀 Requisitos previos

- **Python 3.10+**
- **PostgreSQL 14+**
- **pip** actualizado
- **virtualenv** (opcional pero recomendado)

---

## 📦 Instalación de dependencias

1. Clona el repositorio:

```bash
git clone https://github.com/miguelangelHC/ReadExcelExample.git
cd workers_backend
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del proyecto

workers_backend/
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── config/database.py   # Conexión a PostgreSQL
│   ├── models/              # Modelos SQLAlchemy
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Lógica de negocio
│   ├── routes/              # Endpoints FastAPI
│   └── utils/               # Seguridad y helpers
├── requirements.txt         # Dependencias
├── alembic/                 # Migraciones de BD
└── README.md

---

## ▶️ Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

---
