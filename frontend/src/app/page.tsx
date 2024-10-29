import Link from 'next/link';

export default function Home() {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Bienvenido a AgileBuddy</h1>
          <p className="py-6">
            Tu asistente inteligente para el desarrollo ágil de software. Obtén
            orientación, automatiza tareas y mejora la eficiencia de tu equipo.
          </p>
          <Link href="/chatbot" className="btn btn-primary">
            Iniciar Chat
          </Link>
        </div>
      </div>
    </div>
  );
}
