usando el modelo Ollama (Como lo es el Ollama 3.2 o otros) y una base de datos vectorial como Pinecone o Chroma para la recuperación de información ademas de usar para los Embedding un modelo como lo puede ser el all-MiniLM-L6-v2 de huggingface.

## Análisis del Flujo de Trabajo:
1. *Instalación de Dependencias:*
    Asegúrate de crear un entorno virtual y de configurar un stack tecnológico completo para el desarrollo del proyecto. Todas las dependencias deben estar actualizadas a sus versiones más recientes. Para esto, no especifiques versiones en el archivo requirements.txt para que se instalen automáticamente las últimas versiones de cada librería.
2. *Carga de Documentos:*
   Los documentos PDF de momento solo van a ser de Scrum y mas adelante de implementara informacion sobre las otras metodologías ágiles se cargan desde el directorio data
3. *División de Documentos:*
   Los documentos se dividen en fragmentos manejables utilizando para facilitar el procesamiento y la búsqueda semántica.
4. *Cálculo de Embeddings:*
   Cada fragmento se convierte en un vector numérico utilizando el modelo de all-MiniLM-L6-v2 de la plataforma HuggingFace, lo que permite realizar búsquedas basadas en similitud semántica.
5. *Almacenamiento en Base de Datos Vectorial:*
   Los embeddings y metadatos se almacenan en la base de datos vectorial Chroma o pinecole, lo que permite una recuperación eficiente de información relevante.
6. *Consulta del Chatbot:*
   Cuando un usuario realiza una pregunta, el sistema:
   - Calcula el embedding de la pregunta.
   - Recupera los fragmentos más relevantes de la base de datos.
   - Construye un prompt que incluye el contexto recuperado y la pregunta del usuario.
7. *Generación de Respuestas:*
   El modelo de lenguaje (por ejemplo, Ollama con el modelo "llama 3.2" o mistral") genera una respuesta basada en el prompt construido.
8. *Presentación de la Respuesta:*
   El sistema muestra la respuesta al usuario, incluyendo, si es necesario, las fuentes o referencias de los fragmentos utilizados.
9. *Evaluación y Pruebas:*
   Los scripts de prueba permiten verificar la precisión y relevancia de las respuestas del chatbot, asegurando que cumple con las expectativas.
