// /src/types/chatbot.d.ts
export interface ChatbotMessage {
  id: number;
  text: string;
  sender: 'user' | 'bot';
}

export interface ChatbotContextProps {
  messages: ChatbotMessage[];
  sendMessage: (message: string) => Promise<void>;
  loading: boolean;
}
