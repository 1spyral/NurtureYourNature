import { useState, useEffect } from "react";
import { BACKEND_HOST } from "../config";
import ChatButton from "./ChatButton";

export default function ChatList() {
    const [chats, setChats] = useState([]);
    const [selectedChat, setSelectedChat] = useState(null);

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
        const intervalId = setInterval(getChats, 200);

        return () => clearInterval(intervalId);
    }, []);

    return (
        <div className="chatlist">
            {}
            <div className="chat-header">
                {selectedChat ? `Chat #${selectedChat.id}` : "Select a Chat"}
            </div>
            {}
            {chats.map(chat => (
                <div className = "buttonwrapper" onClick={() => setSelectedChat({ id: chat.id, name: `Chat #${chat.id}` })}>
                <ChatButton 
                    id={chat.id} 
                    name={`Chat #${chat.id}`} 
                    key={chat.id} 
                     
                />
                </div>
            ))}
        </div>
    );
}
