from tools.thread import Thread

class Plant:
    def __init__(self):
        self.threads = []
        self.hp = 100

    def new(self):
        self.threads.append(Thread())
        return len(self.threads) - 1
    
    def create(self, id, message, role = "user"):
        self.threads[id].create(message, role)

    def run(self, id, type = 1):
        return self.threads[id].run(type)
    
plant = Plant()