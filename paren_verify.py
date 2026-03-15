class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # def verify_parentheses(self, data):
    #     counter = 0
    #     other_counter = 0
    #     for caractere in data:
    #         node = Node(caractere)
    #         node.next = self.top
    #         self.top = node
    #         self._size += 1

    #         if caractere == '(':
    #             counter += 1
    #         if caractere == ')':
    #             other_counter += 1

    #     if counter == other_counter: 
    #         print('ta tudo  certo')
    #     else:
    #         print('não ta certo não')

    """
    nova logica

    usar a pilha para adicionar os parenteses '(' encontrados no meio da expressao,
    e com o ')' ir retirando os parenteses, com o metodo pop
    """

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1
            

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next
        self._size = self._size - 1
        return removed.data
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self.top is None
    
def verify_parentheses(data):
    pilha = Stack()

    for caractere in data:
        if caractere == '(':
            pilha.push('(')
        elif caractere == ')':
            if pilha.pop() is None:
                return False
    return pilha.is_empty()

if __name__ == "__main__":

    testes = ["((A+B) * C)", "(A+B))", "((A+B)"]

    for t in testes:
        resultado = "Válido" if verify_parentheses(t) else "Inválido"
        print(f"{t} -> {resultado}")
