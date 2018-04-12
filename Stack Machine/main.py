from Stack import Stack

def popOp():
    print(stack.pop())

def addOp():
      stack.add()

def subOp():
      stack.sub()

def mulOp():
      stack.mul()

def divOp():
      stack.div()

operation =  {
    'pop' : popOp,
    'add' : addOp,
    'sub' : subOp,
    'mul' : mulOp,
    'div'  : divOp,
    }

with open("entrada.txt", "r") as textFile:
    stack = Stack()
    pushOp = False

    for line in textFile:

        for word in line.split():

            if pushOp:
                stack.push(word)
                pushOp = False

            elif word == "push":
                pushOp = True

            else:
                try:
                    operation[word]()
                except KeyError:
                    continue
