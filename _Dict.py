Ticket = input("Enter ticket number: ")
Name = input("Enter staff name: ")

Case = {"Ticket number":Ticket, "Staff name":Name}

for key in Case.keys():
    value = Case[key]
    print(key, "=", value)