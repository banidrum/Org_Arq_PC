class Stack:

    def __init__(self):
        self._data = list()
        self.maxSize = 8
        self.stackPointer = 0

    def push(self, data):
        if self.stackPointer>=self.maxSize:
                return ("Pilha Cheia")
        self._data.append(int(data))
        self.stackPointer += 1

    def pop(self):
          if(self.stackPointer<=0):
                 return ("Pilha Vazia")
          item = self._data.pop()
          self.stackPointer -= 1
          return item

    def size(self):
          return self.stackPointer

    def add(self):
          try:
              i = Stack.pop(self)  +  Stack.pop(self)
              Stack.push(self, i)
          except IndexError:
              return

    def sub(self):
          try:
             i = Stack.pop(self) - Stack.pop(self)
             Stack.push(self, i)
          except IndexError:
              return

    def mul(self):
          try:
             i = Stack.pop(self) * Stack.pop(self)
             Stack.push(self, i)
          except TypeError:
              return

    def div(self):
        try:
            i = Stack.pop(self) / Stack.pop(self)
            Stack.push(self, i)
        except TypeError:
            return
