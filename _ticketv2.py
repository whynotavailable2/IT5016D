def menu():
    print("[1] Create new ticket") #Done
    print("[2] Respond to ticket (by number)")
    print("[3] Reopen resolved ticket")
    print("[4] View all tickets") #Done
    print("[5] Display ticket statistics")
    print("[0] Exit")

menu()
selection = input("Enter selection: ")

try:
    file = open("Ticket.txt", "r")
except FileNotFoundError:
    file = open("Ticket.txt", "x")

if selection == "1": #Create new ticket
    staff_id = str(input("Enter Staff ID: "))
    staff_name = str(input("Enter Staff Name: "))
    staff_email = str(input("Enter Staff Email: "))
    description = str(input("Enter Problem description: "))
    status = str(input("Resolved/Unresolved: "))
    file = open("Ticket.txt", "a")
    file.write(f"\n{staff_id}, {staff_name}, {staff_email}, {description}, {status}")
    file.close()

elif selection == "2": #Respond to ticket (by number)
    print("?")

elif selection == "3": #Reopen resolved ticket
    print("?")

elif selection == "4": #View all tickets
    file = open("Ticket.txt", "r")
    print(file.read())
    file.close()

elif selection == "5": #Display ticket statistics - by counting how many lines total?
    file = open("Ticket.txt", "r")
    print(read.lines)
    print(file.read())
    file.close()

elif selection == "0":
    print("Thank you")
else:
    print("Invalid input.")
