# evaluacionDocker 🐳

Evaluación de un entorno Docker con Flask, Nginx y `docker-compose`.

---

## 📄 Descripción

Este proyecto demuestra una aplicación Python (Flask) contenida en Docker, servida mediante Nginx, y orquestada con `docker-compose`. Incluye los siguientes componentes:

- `app.py`: Servidor web Flask.
- `index.html`: Plantilla estática de ejemplo.
- `Dockerfile`: Construcción de la imagen de la aplicación.
- `Dockerfile.nginx`: Configuración para servir la app con Nginx.
- `.dockerignore`, `.env`, `requirements.txt`, `docker-compose.yml`.

---

## 🚀 Comenzando

### Prerrequisitos

- [Docker](https://www.docker.com/) instalado.
- [Docker Compose](https://docs.docker.com/compose/) disponible.

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/iCruzDaniel/evaluacionDocker.git
   cd evaluacionDocker
   ```

2. Copia (o ajusta) el archivo de variables de entorno:

   ```bash
   cp .env.example .env
   # O modifica manualmente .env según sea necesario
   ```

3. Construye y levanta los contenedores:

   ```bash
   docker-compose up --build -d
   ```

---

## ▶️ Cómo ejecutar

* La app Flask estará disponible en `http://localhost:5000/`
* Nginx expondrá la app en `http://localhost:80/`
* Aplica recarga automática tras cambios en el código (según configuración).

---

## 🧪 Pruebas rápidas

Prueba que todo esté funcionando correctamente:

```bash
curl http://localhost/
```

Deberías ver el contenido de `index.html` servido por Nginx.

---

## 🛠️ Despliegue

Para producción o despliegue externo, puedes:

* Ajustar variables en `.env` (como puertos, modo DEBUG).
* Usar `docker-compose -f docker-compose.yml up -d --remove-orphans`.
* Implementar en un host remoto o servicio de contenedores.

---

## ⚙️ Estructura del repositorio

```
.
├── backend/
│   ├── app.py
│   ├── Dockerfile                # Imagen Flask
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile.nginx         # Imagen Nginx
│   └── index.html
├── .dockerignore
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Tecnologías usadas

* **Python 3** y **Flask** – backend web
* **Nginx** – proxy y servidor estático
* **Docker**, **Docker Compose** – creación y orquestación de contenedores

---

## 🤝 Contribuciones

Se aceptan sugerencias, mejoras o correcciones. Por favor, abre un issue o pull request.

<!-- --- -->

<!-- ## 📝 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE). Dale una lectura para más detalles. -->

---

## 🙏 Agradecimientos

Plantilla adaptada de buenas prácticas de READMEs en GitHub .

---

## 📄 Contacto

Para dudas, sugerencias o colaboración, puedes contactarme vía GitHub.



---

Puedes ajustar los puertos, valores en `.env` y cualquier otra sección según lo necesites.