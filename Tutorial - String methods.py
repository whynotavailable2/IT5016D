#slice operator with colon ::
fruits = ['apples', 'pear', 'peach']
text = 'Hello I like python'
print(text[1:9]) #start:stop:step
print(text[1::2]) #start:stop:step (no stop if blank)


# .strip(), len(), .lower(), .upper(), .split()
text = input('Enter something: ')
print(text.strip())#strips the spaces
print(len(text))#length in letters
print(text.lower())
print(text.upper())
print(text.split('.'))#enter delimiter to split by
print(text.split('-'))
