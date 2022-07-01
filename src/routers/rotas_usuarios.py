from fastapi import APIRouter, status, Depends
from typing import List
from src.schema.schema import Usuario
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorio.repositorio_usuario import RepositorioUsuario



router = APIRouter()



@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def signup(usuario:Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado



@router.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios