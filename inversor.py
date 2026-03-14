class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self): 
        self.top = None
        self._size = 0

    def invert(self, data):
        for letter in data:
            node = Node(letter)
            node.next = self.top
            self.top = node
            self._size += 1
            
        #até aqui ele vai empilhar as letras
        while self.top: #tenho que fazer ele percorrer a palavra inteira até acabar
            print(self.top.data)
            self.top = self.top.next
            



if __name__ == "__main__":
    pilha = Stack()
    palavra = input("Insira uma palavra")
    pilha.invert(palavra)