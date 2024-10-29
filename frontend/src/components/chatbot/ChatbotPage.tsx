'use client';

import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, Bot, User } from 'lucide-react';

interface Message {
  id: number;
  text: string;
  isBot: boolean;
  sources?: string;
}

export default function ChatbotPage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: '¡Hola! Soy AgileBuddy, tu asistente para el desarrollo ágil. ¿En qué puedo ayudarte hoy?',
      isBot: true,
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = {
      id: messages.length + 1,
      text: input,
      isBot: false,
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await axios.post('/api/query', { input: input });
      const botMessage: Message = {
        id: messages.length + 2,
        text: response.data.response,
        isBot: true,
        sources: response.data.sources,
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error al enviar mensaje al chatbot:', error);
      const errorMessage: Message = {
        id: messages.length + 2,
        text: 'Lo siento, ha ocurrido un error. Por favor, intenta de nuevo más tarde.',
        isBot: true,
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-base-200">
      <header className="navbar bg-primary text-primary-content shadow-lg">
        <div className="flex-1">
          <h1 className="text-2xl font-bold">AgileBuddy Chat</h1>
        </div>
      </header>
      <div className="flex-1 overflow-auto p-4 space-y-4">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`chat ${msg.isBot ? 'chat-start' : 'chat-end'}`}
          >
            <div className="chat-image avatar">
              <div className="w-10 rounded-full bg-neutral-focus text-neutral-content grid place-items-center">
                {msg.isBot ? <Bot size={20} /> : <User size={20} />}
              </div>
            </div>
            <div
              className={`chat-bubble ${msg.isBot ? 'chat-bubble-primary' : 'chat-bubble-secondary'}`}
            >
              {msg.text}
            </div>
            {msg.sources && (
              <div className="chat-footer opacity-50 text-xs mt-1">
                Fuentes: {msg.sources}
              </div>
            )}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSendMessage} className="p-4 bg-base-300">
        <div className="join w-full">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Escribe tu mensaje..."
            className="input input-bordered join-item flex-1"
            disabled={isLoading}
          />
          <button
            type="submit"
            className="btn btn-primary join-item"
            disabled={isLoading}
          >
            {isLoading ? (
              <span className="loading loading-spinner"></span>
            ) : (
              <Send size={20} />
            )}
          </button>
        </div>
      </form>
    </div>
  );
}
