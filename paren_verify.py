class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def verify_parentheses(self, data):
        counter = 0
        other_counter = 0
        for caractere in data:
            node = Node(caractere)
            node.next = self.top
            self.top = node
            self._size += 1

            if caractere == '(':
                counter += 1
            if caractere == ')':
                other_counter += 1

        if counter == other_counter: 
            print('ta tudo  certo')
        else:
            print('não ta certo não')



    def push(self, data):
        for letter in data:
            node = Node(letter)
            node.next = self.top
            self.top = node
            self._size += 1
            

    def pop(self, data):
        if self.top is None:
            return None
        removed = self.top
        self.topo = self.topo.next
        self._size = self._size - 1
        return removed.data

"""
nova logica

usar a pilha para adicionar os parenteses '(' encontrados no meio da expressao,
e com o ')' ir retirando os parenteses, com o metodo pop
"""

if __name__ == "__main__":
    pilha = Stack()
    operacao = input("Insira uma operação com parenteses: ")
    pilha.verify_parentheses(operacao)