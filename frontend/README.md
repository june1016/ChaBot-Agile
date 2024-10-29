# Explicación de los archivos del frontend:

```markdown
/Frontend
├── /public
│ └── /assets
│ └── /images # Imágenes utilizadas en la aplicación (logo, iconos de chatbot, etc.)
│ └── /icons # Iconos SVG o PNG utilizados en la interfaz.
├── /src
│ ├── /app
│ │ ├── /chatbot
│ │ │ ├── page.tsx # Página principal del chatbot, renderiza la interfaz del chatbot.
│ │ │ ├── layout.tsx # Layout específico para el chatbot, organiza los componentes dentro del chatbot.
│ │ ├── /api
│ │ │ └── query/route.ts # API del chatbot, maneja las solicitudes al backend y respuestas.
│ │ ├── layout.tsx # Layout general de la aplicación, define la estructura de la aplicación completa.
│ │ └── page.tsx # Página de inicio de la aplicación, vista inicial con el chatbot.
│ ├── /components
│ │ └── /chatbot
│ │ ├── ChatbotPage.tsx # pagina de conversacion del chatbot
│ │ └── /common # Componentes reutilizables de la app
│ ├── /contexts
│ │ └── ChatbotProvider.tsx # Proveedor que maneja el estado global del chatbot, incluido el historial de mensajes. (FALTA)
│ ├── /hooks
│ │ └── useChatbot.tsx # Hook personalizado que gestiona la lógica de interacción del chatbot con el backend. (FALTA)
│ ├── /styles
│ │ ├── globals.css # Estilos globales de la aplicación, incluye Tailwind CSS y DaisyUI.
│ │ ├── chatbot.css # Estilos específicos para el chatbot (si es necesario personalizar más allá de DaisyUI). (FALTA)
│ ├── /utils
│ │ ├── helpers.ts # Funciones auxiliares para manejar datos y lógica repetitiva. (FALTA)
│ ├── /types
│ └── chatbot.d.ts # Definiciones de tipos para el chatbot, utilizadas en TypeScript. (FALTA)
├── next.config.js # Archivo de configuración para Next.js, puede incluir configuraciones del App Directory.
├── tsconfig.json # Archivo de configuración para TypeScript, define las opciones de compilación.
├── package.json # Contiene dependencias y scripts del proyecto (como los scripts de lint y format).
└── Resto de archivos de configuracion...
```
