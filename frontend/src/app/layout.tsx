import '../styles/globals.css';
import { Providers } from './providers';
import { ReactNode } from 'react';
import Link from 'next/link';

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <html lang="es" data-theme="cupcake">
      <head>
        <title>AgileBuddy - Asistente para Metodologías Ágiles</title>
      </head>
      <body className="bg-base-200">
        <Providers>
          <div className="drawer lg:drawer-open">
            <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
            <div className="drawer-content flex flex-col">
              <div className="w-full navbar bg-base-300 lg:hidden">
                <div className="flex-none lg:hidden">
                  <label
                    htmlFor="my-drawer-2"
                    className="btn btn-square btn-ghost"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      className="inline-block w-6 h-6 stroke-current"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M4 6h16M4 12h16M4 18h16"
                      ></path>
                    </svg>
                  </label>
                </div>
                <div className="flex-1 px-2 mx-2">AgileBuddy</div>
              </div>
              {children}
            </div>
            <div className="drawer-side">
              <label htmlFor="my-drawer-2" className="drawer-overlay"></label>
              <ul className="menu p-4 w-80 h-full bg-base-200 text-base-content">
                <li className="mb-4">
                  <Link href="/" className="text-xl font-bold">
                    AgileBuddy
                  </Link>
                </li>
                <li>
                  <Link href="/chatbot">Chatbot</Link>
                </li>
                {/* Añade más enlaces de navegación aquí si es necesario */}
              </ul>
            </div>
          </div>
        </Providers>
      </body>
    </html>
  );
}
