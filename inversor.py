class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self): 
        self.top = None
        self._size = 0

    def push(self, data):
        for letter in data:
            node = Node(letter)
            node.next = self.top
            self.top = node
            self._size += 1
            
    def invert(self):
        while self.top:
            print(self.top.data)
            self.top = self.top.next
            

if __name__ == "__main__":
    pilha = Stack()
    palavra = input("Insira uma palavra")
    pilha.push(palavra)
    pilha.invert()