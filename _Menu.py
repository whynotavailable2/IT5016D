#Creates menu
def menu():
    print("[1] Submit ticket")
    print("[2] Show all tickets")
    print("[3] Respond to ticket")
    print("[4] Reopen resolved ticket")
    print("[5] Display ticket statistics")
    print("[0] Exit")

#Runs menu with input
menu()
option = int(input("Enter selection: "))

#Loop unless 0 is selected
while option != 0:
    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        print("Invalid selection")
    menu()
    option = int(input("Enter selection: "))