test = 9

def funlocalis5(x):
    test = 5
    print(test)

funlocalis5(1)

def funglobal(x):
    print(test)

funglobal(2)

def funglobalchangeto7(x):
    global test
    test = 7
    print(test)

funglobalchangeto7(5)
