from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_auth, rotas_pedidos


app = FastAPI()

# CORS

origins = ['http://localhost:3000']

app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"] )

# ROTAS PRODUTOS

app.include_router(rotas_produtos.router)

# ROTAS SEGURANÇA: Autenticação e autorização

app.include_router(rotas_auth.router, prefix="/auth")


# ROTAS PEDIDOS 

app.include_router(rotas_pedidos.router)