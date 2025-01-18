import { useState, useEffect } from "react";
import { BACKEND_HOST } from "../config";
import ChatButton from "./ChatButton";


export default function ChatList() {
    const [chats, setChats] = useState([]);

    async function getChats() {
        try {
            const response = await fetch(BACKEND_HOST + "/api/chats");
            if (!response.ok) {
                throw new Error(`Error fetching from backend: Status: ${response.status}`);
            }
            const result = await response.json();
            setChats(result);
        } catch (error) {
            console.error(error);
        }
    }    

    useEffect(() => {
        const intervalId = setInterval(getChats, 3000);

        return () => clearInterval(intervalId);
    }, []);

    return (
        <div className="chatlist">
            {chats.map(chat => {
                <ChatButton id={chat.id} name={chat.name} key={chat.id} />
            })}
        </div>
    )
}