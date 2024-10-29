import dynamic from 'next/dynamic';

const ChatbotPage = dynamic(
  () => import('../../components/chatbot/ChatbotPage'),
  { ssr: false }
);

export default function Page() {
  return <ChatbotPage />;
}
