import useStore from "../store"
import { BACKEND_HOST } from "../config";
import { useEffect, useState } from "react";
import Message from "./Message";

export default function Chat() {
    const { chatId } = useStore();
    const [messages, setMessages] = useState([]);


    useEffect(() => {
        async () => {
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
    }, [chatId]);


    if (chatId === null) {
        return (
            <div>
                null chat
            </div>
        )
    } else {
        return (
            <div>
                {messages.map((message, index) => <Message key={index} />)}
            </div>
        )
    }
}