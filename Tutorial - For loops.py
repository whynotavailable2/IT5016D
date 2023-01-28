#Basic for loops
for x in range (0, 5, 1): #start, stop, step
    print (x)

input('Now on to foods example. Press any key when ready.')

#More advanced

foods = ['rice', 'egg', 'bottle']
for food in foods:
    print(food)
#Does the plural "s" really tell it what to do?
    
input('Which are edible/inedible? Press any key when ready.')

for food in foods:
    if food == 'bottle':
        print('inedible')
    else:
        print('edible')
        
#More advanced        
input('Which are allergens? Press any key when ready.')

for x in range(0, 3):
    if foods[x] == 'egg':
        print('Warning! Allergen detected')
    else:
        print('Safe')
