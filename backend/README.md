### *Explicación de los archivos y su función*

---

#### *1. backend\load_documents.py*
*Propósito:*  
Este archivo carga los documentos PDF desde la carpeta data/, los divide en fragmentos manejables y luego genera embeddings para cada fragmento. Finalmente, los fragmentos con sus embeddings se almacenan en una base de datos vectorial utilizando *Chroma*. 

*Proceso:*
1. *Carga de PDFs:* Usa PyPDFLoader para cargar y extraer el contenido de los PDFs.
2. *División de texto:* Utiliza RecursiveCharacterTextSplitter para dividir los documentos en fragmentos de 1000 caracteres con superposición de 200 caracteres.
3. *Embeddings:* Genera los embeddings usando el modelo all-MiniLM-L6-v2.
4. *Base de datos vectorial:* Crea una colección en Chroma y almacena los fragmentos con sus embeddings para consultas futuras.

*Resultado:*  
Guarda los fragmentos procesados en *Chroma* para su uso en el chatbot o en futuras consultas. 

---

#### *2. backend\inspect_chroma.py*
*Propósito:*  
Permite inspeccionar los documentos y metadatos almacenados en la base de datos vectorial de Chroma.

*Proceso:*
1. *Cargar la base de datos:* Conecta a la base de datos Chroma.
2. *Obtener documentos y metadatos:* Recupera el contenido y los metadatos de los fragmentos almacenados.
3. *Mostrar resultados:* Imprime en consola los nombres de los archivos originales y una vista previa del contenido de cada fragmento.

*Resultado:*  
Permite verificar que los fragmentos y metadatos fueron correctamente almacenados y acceder al contenido que estará disponible para consultas en el chatbot.

---

#### *3. backend\chatbot.py*
*Propósito:*  
Implementa un chatbot conversacional utilizando la base de datos vectorial Chroma y un modelo de lenguaje *Ollama* (Llama2). Este chatbot responde preguntas sobre los documentos almacenados y proporciona las fuentes de las respuestas.

*Proceso:*
1. *Carga de la base de datos Chroma:* Conecta con la base de datos y carga los embeddings.
2. *Configuración del modelo LLM:* Usa el modelo Llama2 de Ollama para generar respuestas.
3. *Cadena conversacional:* Utiliza ConversationalRetrievalChain para consultar la base de datos Chroma y generar respuestas basadas en los documentos.
4. *Interacción con el usuario:* Recoge la entrada del usuario, busca la respuesta en la base de datos y devuelve la respuesta junto con las fuentes utilizadas.

*Resultado:*  
El chatbot responde preguntas del usuario con base en los documentos cargados y proporciona las fuentes relevantes.

---

### *Librerías esenciales del proyecto*

1. *LangChain:*  
   - Provee herramientas para trabajar con modelos de lenguaje, embeddings y bases de datos vectoriales.
   - *Subcomponentes usados:* 
     - langchain.embeddings: Para generar embeddings.
     - langchain.vectorstores: Para manejar bases de datos vectoriales (Chroma).
     - langchain.chains: Para construir cadenas conversacionales.

2. *Chroma (chromadb):*  
   - Almacena los embeddings de los documentos y permite búsquedas por similitud.

3. *HuggingFace Transformers:*  
   - Carga el modelo all-MiniLM-L6-v2 para generar embeddings.

4. *Ollama:*  
   - Ejecuta el modelo de lenguaje Llama2, encargado de responder las preguntas del chatbot.

5. *FastAPI (Pendiente de integración):*  
   - Proveerá una API para conectar el backend con el *frontend* en React, permitiendo que las consultas del chatbot se realicen desde una interfaz web.

---

### *Conexión con el Frontend mediante API*

  Implementado con *FastAPI* para los endpoints del chatbot y permitir que el frontend en React realice consultas al backend.

---

### *Próximos pasos y correcciones pendientes*

1. *Implementar API con FastAPI:*
   - Crear endpoints para recibir preguntas y devolver respuestas desde el frontend.

2. *Optimización de almacenamiento:*
   - Asegurarse de que cada fragmento tiene su embedding correspondiente para evitar errores.

3. *Validar manejo de errores:*
   - Mejorar las excepciones para detectar fallas en tiempo de ejecución.

4. *Verificar persistencia en Chroma:*
   - Confirmar que todos los documentos se almacenan y recuperan correctamente.

---

### *Conclusión*
Este proyecto utiliza modelos de lenguaje y bases de datos vectoriales para crear un chatbot basado en documentos. A través de *Chroma* se almacenan los documentos y sus embeddings, permitiendo búsquedas eficientes por similitud. El chatbot se conecta a un modelo Llama2 para responder preguntas y pronto se integrará con un frontend en React mediante *FastAPI*.

Este flujo asegura que las respuestas del chatbot estén respaldadas por los documentos cargados, aumentando la precisión y confiabilidad del sistema.
