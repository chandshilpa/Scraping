import outputtext
class Person:
    totalPeople = 0 
    def __init__(self):
        self.name = "" 
        self.address = "" 
        self.phone = "" 

        Person.totalPeople = Person.totalPeople + 1 

    def setName(self, name):
        self.name = name 

    def setAddress(self, address):
        address = " ".join(address.split('\n'))
        self.address = address 

    def setPhone(self, phone): 
        self.phone = phone 

    def saveRecord(self, outputFile): 
        row = list()
        row.append(self.name) 
        row.append(self.address) 
        row.append(self.phone)

        outputFile.appendRow(row)
        outputtext.outputText = outputtext.outputText + ("Person : {} saved.\n".format(str(row)))
        outputtext.outputLabel.config(text=outputtext.outputText)



    
