listofmacs = []
with open("Ticket.txt", "r") as reader:
    for line in reader.readlines():
        listofmacs.append(line)

ID_num = 12345

name = str('john')

newpass = str(ID_num)[:2],name[:3]
join = ""

print('Your new password is', join.join(newpass))

dictionary = {}
dictionary['a'] = [1,2,3,4]
dictionary['b'] = [5,6,7,8]
listd = list(dictionary.keys())
print(listd)
for keys, value in dictionary.items():
    print(keys)

case_num = input('Please enter a ticket number to check its statistics.')
print('Ticket number:', case_num)
print('Name:', dictionary[case_num][1])

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
