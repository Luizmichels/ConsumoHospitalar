from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.core.security import verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    usuario = (
        db.query(Usuario).filter(Usuario.email == email, Usuario.ativo == True).first()
    )

    if not usuario or not verificar_senha(senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token(
        {
            "sub": str(usuario.id),
            "empresa_id": usuario.empresa_id,
            "perfil": usuario.perfil,
        }
    )
    return {"access_token": token, "token_type": "bearer"}
