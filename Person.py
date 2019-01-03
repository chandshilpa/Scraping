class Person: 
    totalPeople = 0 

    def __init__(self):
        self.name = "" 
        self.address = "" 
        self.phone_no = ""

        Person.totalPeople = Person.totalPeople + 1 

    def setName(self, name):
        self.name = name 

    def setAddress(self, address):
        address = " ".join(address.split('\n'))
        self.address = address 

    def setPhone(self, phone_no):
        self.phone_no = phone_no

    def saveRecord(self, outputFile):
        row = list()
        row.append(self.name)
        row.append(self.address)
        row.append(self.phone_no)

        outputFile.appendRow(row)
        print("Person : {} saved.".format(str(row)))









