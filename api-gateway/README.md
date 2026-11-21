# Proyecto: Microservicios + API Gateway

## Universidad Americana (UAM)
Carrera: Ingeniería en Sistemas

Asignatura: Desarrollo de Aplicaciones de Última Generación

## Integrantes
- Heiner
- Stefan
- Jarvio

## Descripción del proyecto

Este proyecto demuestra una arquitectura basada en microservicios
utilizando Python, FastAPI, Docker y Nginx como API Gateway.

El sistema está compuesto por dos microservicios independientes:

1. Microservicio de Usuarios:
   Permite registrar y consultar usuarios.

2. Microservicio de Pedidos:
   Permite registrar y consultar pedidos.
   Se comunica con el microservicio de usuarios para verificar
   que el usuario exista antes de registrar un pedido.

El API Gateway centraliza el acceso a ambos microservicios.

## Tecnologías utilizadas

- Python
- FastAPI
- Docker
- Docker Compose
- Nginx
- Swagger
- HTTP y JSON

## Estructura del proyecto

Microservicios_API_Gateway/
│
├── usuarios-service/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── pedidos-service/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── api-gateway/
│   └── nginx.conf
│
├── evidencias/
│
├── docker-compose.yml
│
└── README.md

## Requisitos

- Docker Desktop instalado.
- Docker Compose disponible.
- Puertos 8001, 8002 y 8085 libres.

## Instrucciones para ejecutar el proyecto

1. Abrir Docker Desktop.

2. Abrir una terminal en la carpeta principal del proyecto.

3. Ejecutar el siguiente comando:

   docker compose up -d --build

4. Esperar a que los contenedores se inicien.

5. Verificar su estado:

   docker compose ps

## Direcciones del sistema

API Gateway:
http://localhost:8085/

Consultar usuarios mediante Gateway:
http://localhost:8085/usuarios

Consultar pedidos mediante Gateway:
http://localhost:8085/pedidos

Swagger de Usuarios:
http://localhost:8001/docs

Swagger de Pedidos:
http://localhost:8002/docs

## Prueba de funcionamiento

1. Abrir Swagger de Usuarios.
2. Utilizar POST /usuarios para registrar un usuario.
3. Abrir Swagger de Pedidos.
4. Utilizar POST /pedidos para crear un pedido.
5. El microservicio de pedidos verifica que el usuario exista.
6. Consultar los registros mediante el API Gateway.

## Arquitectura

Cliente
   |
   v
API Gateway (Nginx)
   |
   |---------------------|
   |                     |
   v                     v
Microservicio         Microservicio
de Usuarios           de Pedidos
   ^                     |
   |_____________________|

El microservicio de pedidos consulta al de usuarios
para validar la existencia de un usuario.

## Separación de responsabilidades

Cada microservicio tiene una responsabilidad específica.

El microservicio de usuarios administra los usuarios.

El microservicio de pedidos administra los pedidos.

El API Gateway recibe las solicitudes y las dirige
al microservicio correspondiente.

## Almacenamiento de datos

Esta versión utiliza almacenamiento temporal en memoria.

Los datos registrados se pierden cuando se reinician
los procesos de los microservicios.

## Detener el proyecto

Desde la carpeta principal, ejecutar:

docker compose down

Este comando detiene y elimina los contenedores
del proyecto sin eliminar el código fuente.