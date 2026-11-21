from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import httpx
import os

app = FastAPI(
    title="Microservicio de Pedidos",
    description="API para gestionar pedidos",
    version="1.0.0"
)

# Dirección del microservicio de usuarios
# Funciona tanto en Windows como en Docker
USUARIOS_SERVICE_URL = os.getenv(
    "USUARIOS_SERVICE_URL",
    "http://127.0.0.1:8001"
)


# Modelo de pedido
class Pedido(BaseModel):
    usuario_id: int
    producto: str
    cantidad: int = Field(gt=0)
    precio: float = Field(gt=0)


# Almacenamiento temporal
pedidos = {}
contador_id = 1


# Endpoint principal
@app.get("/")
def inicio():
    return {
        "mensaje": "Microservicio de Pedidos funcionando correctamente"
    }


# Crear pedido
@app.post("/pedidos")
def crear_pedido(pedido: Pedido):
    global contador_id

    # Verificar que el usuario existe
    try:
        respuesta = httpx.get(
            f"{USUARIOS_SERVICE_URL}/usuarios/{pedido.usuario_id}",
            timeout=5.0
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="No se pudo conectar con el microservicio de usuarios"
        )

    if respuesta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="El usuario indicado no existe"
        )

    if respuesta.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Error al consultar el microservicio de usuarios"
        )

    usuario = respuesta.json()

    # Crear el pedido
    nuevo_pedido = {
        "id": contador_id,
        "usuario_id": pedido.usuario_id,
        "nombre_usuario": usuario["nombre"],
        "producto": pedido.producto,
        "cantidad": pedido.cantidad,
        "precio": pedido.precio,
        "total": round(pedido.cantidad * pedido.precio, 2)
    }

    pedidos[contador_id] = nuevo_pedido
    contador_id += 1

    return {
        "mensaje": "Pedido registrado correctamente",
        "pedido": nuevo_pedido
    }


# Consultar todos los pedidos
@app.get("/pedidos")
def obtener_pedidos():
    return list(pedidos.values())


# Buscar pedido por ID
@app.get("/pedidos/{pedido_id}")
def obtener_pedido(pedido_id: int):

    if pedido_id not in pedidos:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return pedidos[pedido_id]