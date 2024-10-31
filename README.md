# Chatbot basado en RAG para Metodologías Ágiles

Este proyecto implementa un **chatbot inteligente** utilizando la técnica **Retrieval-Augmented Generation (RAG)** para asistir en la adopción de metodologías ágiles como **Scrum, Kanban y XP**. El chatbot combina un **backend** construido con Python, LangChain y FastAPI, y un **frontend** desarrollado en **Next.js**, lo que permite una experiencia interactiva y dinámica para el usuario.

---

## Requisitos Previos

### 1. Instalación de dependencias para el Backend

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Crear un entorno virtual e instalar dependencias:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   .\venv\Scripts\activate  # En Windows

   pip install -r backend/requirements.txt
   ```

3. **Colocar archivos PDF:**  
   Coloca los documentos en `backend/data/`. Estos serán la fuente de información para el chatbot.

---

### 2. Instalación de dependencias para el Frontend

1. **Acceder al directorio del frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar las dependencias del proyecto:**
   ```bash
   npm install
   ```

---

## Estructura del Proyecto

- **backend/data**: Contiene los archivos PDF con información relevante sobre metodologías ágiles.
- **backend/load_documents.py**: Carga e indexa documentos en la base de datos vectorial Chroma.
- **backend/chatbot.py**: Lógica del chatbot usando RAG para la recuperación de información.
- **backend/inspect_chroma.py**: Herramienta para inspeccionar los documentos almacenados en la base de datos Chroma.
- **frontend**: Aplicación en Next.js que ofrece una interfaz para interactuar con el chatbot.

---

## Configuración y Ejecución

### 1. Cargar Documentos

Ejecuta el siguiente comando para cargar los documentos e indexarlos en Chroma:
```bash
python backend/load_documents.py
```
Si los documentos no se encuentran, se notificará mediante un mensaje de error en la consola.

---

### 2. Inspeccionar los Documentos (Opcional)

Este paso permite verificar que los documentos fueron correctamente almacenados en la base de datos Chroma:
```bash
python backend/inspect_chroma.py
```

---

### 3. Iniciar el Backend

Desde la raíz del proyecto, inicia el servidor FastAPI:
```bash
uvicorn backend.chatbot:app --reload
```
El backend estará disponible en:
```
http://localhost:8000
```

---

### 4. Iniciar el Frontend

Accede al directorio del frontend:
```bash
cd frontend
```

Inicia la aplicación de Next.js:
```bash
npm run dev
```
El frontend estará disponible en:
```
http://localhost:3000
```

---

### 5. Interacción con el Chatbot

Desde el frontend, ingresa a `http://localhost:3000` y realiza preguntas relacionadas con metodologías ágiles, como:
- _“¿Qué es Scrum?”_  
- _“¿Cuáles son los beneficios de Kanban?”_

El chatbot responderá usando información cargada en la base de datos vectorial. Además, mostrará la fuente de donde se extrajo la información.

---

## Errores Comunes

1. **Archivos PDF no encontrados:**  
   Verifica que los documentos estén en `backend/data/`.

2. **Número de embeddings no coincide:**  
   Asegúrate de que los documentos se carguen e indexen correctamente.

3. **Conexión fallida entre frontend y backend:**  
   Verifica que ambos servidores (backend y frontend) estén en ejecución y disponibles en los puertos correspondientes.

---

## Próximos Pasos

- Optimizar la generación de respuestas basadas en los documentos cargados.
- Agregar más documentos relevantes sobre metodologías ágiles.
- Realizar pruebas finales y evaluar el desempeño del sistema para identificar mejoras.

---

## Licencia
Falta
---

## Integrantes
- Kevin Rentenria
- Juan Paja
