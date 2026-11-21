from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Microservicio de Usuarios",
    description="API para gestionar usuarios",
    version="1.0.0"
)

class Usuario(BaseModel):
    nombre: str
    correo: str

usuarios = {}
contador_id = 1


@app.get("/")
def inicio():
    return {
        "mensaje": "Microservicio de Usuarios funcionando correctamente"
    }


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    global contador_id

    nuevo_usuario = {
        "id": contador_id,
        "nombre": usuario.nombre,
        "correo": usuario.correo
    }

    usuarios[contador_id] = nuevo_usuario
    contador_id += 1

    return {
        "mensaje": "Usuario registrado correctamente",
        "usuario": nuevo_usuario
    }


@app.get("/usuarios")
def obtener_usuarios():
    return list(usuarios.values())


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):

    if usuario_id not in usuarios:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuarios[usuario_id]