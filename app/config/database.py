# app/config/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a PostgreSQL
# Cambia 'user', 'password', 'localhost' y 'workers' por tus valores reales
DATABASE_URL = "postgresql+psycopg2://user:postgres@localhost:5432/workers"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear la sesión (manejo de transacciones)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos
Base = declarative_base()

# Dependencia para obtener sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
