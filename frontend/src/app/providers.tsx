// /src/app/providers.tsx
import { ReactNode } from 'react';

interface ProvidersProps {
  children: ReactNode;
}

// Este componente envolverá la aplicación con todos los proveedores de contexto global
export function Providers({ children }: ProvidersProps) {
  return (
    <>
      {/* Aquí puedes añadir proveedores en el futuro si los necesitas */}
      {children}
    </>
  );
}
