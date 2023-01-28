#Creating the class "Ticket"
class Ticket:
    count = 0
    def __init__(self, staff_id, name, email, description):
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.description = description
        Ticket.count = Ticket.count + 1

    def displayTotal(self):
        print("Total number of tickets:", self.count)

    def displayTicket(self):
        print("Ticket entered by:")
        print("Staff ID:", self.staff_id)
        print("Staff name:", self.name)
        print("Staff email:", self.email)
        print("Problem description:", self.description)
