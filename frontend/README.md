###

src/
│
├── actions/ # Acciones para manejar el estado global o interacciones complejas
├── app/ # Configuración y lógica de la aplicación (p.ej., configuración de Next.js)
├── components/ # Componentes reutilizables de la interfaz de usuario
├── config/ # Configuraciones generales (p.ej., variables de entorno, rutas API)
├── data/ # Datos estáticos o archivos JSON que no cambian
├── helpers/ # Funciones específicas para tareas concretas
├── hooks/ # Custom hooks de React
├── pages/ # Páginas de Next.js
├── public/ # Archivos estáticos (imágenes, fuentes, etc.)
├── styles/ # Archivos CSS o configuraciones de Tailwind
├── types/ # Definiciones de TypeScript para tipado estático
├── utils/ # Funciones utilitarias generales
└── tests/ # Pruebas unitarias y de integración

### 
/Frontend
  ├── /public
  │     └── /assets
  │           └── /images                # Imágenes utilizadas en la aplicación (logo, iconos de chatbot, etc.).
  │           └── /icons                 # Iconos SVG o PNG utilizados en la interfaz.
  ├── /src
  │     ├── /app
  │     │     ├── /chatbot
  │     │     │     ├── page.tsx         # Página principal del chatbot, renderiza la interfaz del chatbot. (FALTA POR HACER)
  │     │     │     ├── layout.tsx       # Layout específico para el chatbot, organiza los componentes dentro del chatbot. (FALTA POR HACER)
  │     │     ├── /api
  │     │     │     └── chatbot/route.ts # API del chatbot, maneja las solicitudes al backend y respuestas. (FALTA TAMBIEN)
  │     │     ├── layout.tsx             # Layout general de la aplicación, define la estructura de la aplicación completa. 
  │     │     └── page.tsx               # Página de inicio de la aplicación, puede ser la vista inicial con el chatbot. (Falta por hacer)
  │     ├── /components
  │     │     └── /chatbot
  │     │           ├── ChatInput.tsx    # Campo de entrada donde el usuario introduce sus mensajes. 
  │     │           ├── ChatWindow.tsx   # Ventana principal del chatbot donde se muestran las conversaciones.
  │     │           ├── MessageBubble.tsx# Componente para mostrar los mensajes dentro de la ventana del chatbot.
  │     │     └── /common
  │     │           ├── Button.tsx       # Componente de botón reutilizable estilizado con DaisyUI. (Falta)
  │     │           ├── Card.tsx         # Componente de tarjeta, puede ser usado para mostrar información adicional en el chat. (Falta)
  │     ├── /contexts
  │     │     └── ChatbotProvider.tsx    # Proveedor que maneja el estado global del chatbot, incluido el historial de mensajes.
  │     ├── /hooks
  │     │     └── useChatbot.tsx         # Hook personalizado que gestiona la lógica de interacción del chatbot con el backend. (Falta)
  │     ├── /styles
  │     │     ├── globals.css            # Estilos globales de la aplicación, incluye Tailwind CSS y DaisyUI.
  │     │     ├── chatbot.css            # Estilos específicos para el chatbot (si es necesario personalizar más allá de DaisyUI).
  │     ├── /utils
  │     │     ├── helpers.ts             # Funciones auxiliares para manejar datos y lógica repetitiva. (Falta)
  │     │     ├── api.ts                 # Funciones para hacer peticiones HTTP al backend del chatbot.
  │     ├── /types
  │           └── chatbot.d.ts           # Definiciones de tipos para el chatbot, utilizadas en TypeScript. (Falta)
  ├── next.config.js                     # Archivo de configuración para Next.js, puede incluir configuraciones del App Directory.
  ├── tsconfig.json                      # Archivo de configuración para TypeScript, define las opciones de compilación.
  ├── package.json                       # Contiene dependencias y scripts del proyecto (como los scripts de lint y format).
  └── Resto de archivos de configuracion...
