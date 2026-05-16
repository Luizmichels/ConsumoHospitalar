from fastapi import FastAPI
from app.routers import (
    auth,
    usuarios,
    empresas,
    importacoes,
    previsoes,
    dashboard,
    exportacoes,
)

app = FastAPI(title="MedStock AI", version="1.0.0")

app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(empresas.router)
app.include_router(importacoes.router)
app.include_router(previsoes.router)
app.include_router(dashboard.router)
app.include_router(exportacoes.router)
