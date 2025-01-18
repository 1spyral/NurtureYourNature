import { create } from "zustand";

const useStore = create(set => ({
    chatId: null,
    setChatId: chatId => set(() => ({ chatId }))
}));

export default useStore;