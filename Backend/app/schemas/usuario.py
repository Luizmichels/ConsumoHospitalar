from pydantic import BaseModel, EmailStr
from typing import Literal


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: Literal["admin", "usuario"]


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str
    ativo: bool

    model_config = {"from_attributes": True}
