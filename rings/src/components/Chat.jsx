import useStore from "../store"
import { BACKEND_HOST } from "../config";
import { useEffect, useState } from "react";
import Message from "./Message";

export default function Chat() {
    const { chatId } = useStore();
    const [messages, setMessages] = useState([]);

    async function getChat() {
        if (chatId == null) {
            return
        }
        try {
            const response = await fetch(`${BACKEND_HOST}/api/chat?chatId=${chatId}`);
            if (!response.ok) {
                throw new Error(`Error fetching from backend: Status: ${response.status}`);
            }
            const result = await response.json();
            setMessages(result);
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
        const intervalId = setInterval(getChat, 200)
        
        return () => clearInterval(intervalId);
    }, [chatId]);


    if (chatId === null) {
        return (
            <div className="chat">
                Select a chat
            </div>
        )
    } else {
        return (
            <div className="chat">
                {messages.slice().reverse().map((message, index) => <Message role={message.role} content={message.content} key={index} />)}
            </div>
        )
    }
}