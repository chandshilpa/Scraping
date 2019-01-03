import outputtext
class Person:
    totalPeople = 0

    def __init__(self):
        self.name = ""
        self.location = ""
        self.phone_no = ""

        Person.totalPeople = Person.totalPeople + 1

    def setName(self, name):
        self.name = name

    def setAddress(self, location):
        address = " ".join(location.split('\n'))
        self.address = address

    def setPhone(self, phone_no):
        self.phone_no = phone_no

    def saveRecord(self, outputFile):
        row = list()
        row.append(self.name)
        row.append(self.location)
        row.append(self.phone_no)

        outputFile.appendRow(row)
        outputtext.outputText = outputtext.outputText + ("Person : {} saved.\n".format(str(row)))
        outputtext.outputLabel.config(text=outputtext.outputText)









