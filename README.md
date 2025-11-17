# Proyecto Flask con CI/CD

Este proyecto es una aplicación web simple construida con Flask que muestra un mensaje de "Hola Mundo". Incluye un ciclo completo de Integración Continua (CI) y Despliegue Continuo (CD) utilizando GitHub Actions, con pruebas automatizadas y construcción de un paquete Docker.

## Descripción del Ciclo CI/CD

El ciclo de CI/CD en este proyecto se divide en las siguientes fases:

### 1. Integración Continua (CI)
- **Trigger**: Se activa automáticamente en cada push a la rama `main` o en pull requests.
- **Instalación de dependencias**: Se instalan las dependencias de Python listadas en `requirements.txt`.
- **Ejecución de pruebas**: Se ejecutan pruebas unitarias utilizando pytest para asegurar que el código funcione correctamente.
- **Linting y verificación**: Se verifica la calidad del código (opcional, pero recomendado).

### 2. Construcción del Paquete
- **Construcción de imagen Docker**: Se construye una imagen Docker basada en el `Dockerfile` proporcionado.
- **Empaquetado**: La imagen Docker actúa como el "paquete" final, que puede ser desplegado en cualquier entorno compatible con Docker.

### 3. Despliegue Continuo (CD)
- **Despliegue automático**: En caso de éxito en CI, la imagen Docker se puede desplegar automáticamente a un servicio como Render, Heroku o un clúster Kubernetes.
- **Monitoreo**: El despliegue incluye verificación de que la aplicación esté corriendo correctamente.

## Ejemplo Práctico

### Paso 1: Configuración del Repositorio
1. Crea un repositorio en GitHub.
2. Clona el repositorio localmente:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

### Paso 2: Estructura del Proyecto
- `app.py`: Código principal de la aplicación Flask.
- `requirements.txt`: Dependencias de Python.
- `Dockerfile`: Instrucciones para construir la imagen Docker.
- `tests/`: Directorio con pruebas unitarias.
- `.github/workflows/ci-cd.yml`: Workflow de GitHub Actions.

### Paso 3: Ejecución Local
1. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Ejecuta la aplicación:
   ```
   python app.py
   ```
3. Accede a `http://localhost:5000` para ver "¡Hola Mundo! Soy Edison Flores🚀".

### Paso 4: Pruebas
Ejecuta las pruebas con pytest:
```
pytest
```
Esto debería pasar todas las pruebas unitarias definidas en `tests/test_app.py`.

### Paso 5: Construcción del Paquete
Construye la imagen Docker:
```
docker build -t mi-app-flask .
```
Ejecuta el contenedor:
```
docker run -p 5000:5000 mi-app-flask
```

### Paso 6: CI/CD con GitHub Actions
El workflow en `.github/workflows/ci-cd.yml` automatiza:
- Instalación de dependencias.
- Ejecución de pruebas.
- Construcción de la imagen Docker.
- (Opcional) Push a Docker Hub o despliegue a un servicio.

Ejemplo de salida exitosa en GitHub Actions:
```
Run pytest
============================= test session starts ==============================
collected 2 items

tests/test_app.py::test_hello PASSED
tests/test_app.py::test_hello_content PASSED

========================== 2 passed in 0.12s ============================
```

## Pruebas Incluidas
- **Prueba unitaria básica**: Verifica que la ruta `/` responda correctamente.
- **Prueba de contenido**: Asegura que el mensaje contenga el texto esperado.

## Construcción del Package
El "package" en este proyecto es la imagen Docker, que encapsula la aplicación y sus dependencias. Se construye automáticamente en el pipeline de CI/CD y puede ser desplegada directamente.

## Despliegue Actual
La aplicación está desplegada en: https://edisonflores.onrender.com/

## Repositorio
[Enlace al repositorio en GitHub](https://github.com/tu-usuario/tu-repositorio) (actualizar con el enlace real después de crear el repo).
