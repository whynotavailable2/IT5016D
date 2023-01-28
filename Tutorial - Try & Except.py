text = input('Choose username: ')
try:
    number = int(text)
    print(text, 'is available')
except:
    print(text, 'is not a number')
