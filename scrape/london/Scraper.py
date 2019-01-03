from urllib3 import PoolManager 
from certifi import where
from bs4 import BeautifulSoup 
from time import sleep 

from Person import Person 

class Scraper:
    def __init__(self, name, location, street): 
        self.http = PoolManager(
                    cert_reqs = "CERT_REQUIRED", 
                    ca_certs = where() 
                )
        self.page = 1 
        self.url = "https://thephonebook.bt.com/Person/PersonSearch/"
        self.name = "?Surname={}".format(name) 
        self.location = "&Location={}".format(location) 
        self.street = "&Street={}".format(street) 
        self.pageNumber = "&PageNumber={}".format(self.page) 

    def getPage(self): 
        self.pageCode = self.http.request("GET", "{}{}{}{}{}".format(self.url, self.name, self.location, self.street, self.pageNumber)) 

    def parsePage(self):
        self.code = BeautifulSoup(self.pageCode.data, "html.parser") 

    def getPeopleInfo(self, outputFile): 
        divs = self.code.find_all('div', class_="mb-3 border border-dark px-3") 
        if len(divs) == 0:
            raise Exception("No more records found. Total {} records found.".format(str(Person.totalPeople))) 

        for div in divs: 
            person = Person()
            rows = div.find_all('div', class_="row", recursive=False) 
            
            row0span = rows[0].find('span', class_="black medium")
            person.setName(row0span.text.strip()) 

            row1col8div = rows[1].find('div', class_="col-8 py-2") 
            person.setAddress(row1col8div.text.strip()) 

            person.setPhone(rows[2].find('div', class_="ml-3 d-inline light-blue my-auto no-wrap").text.strip())

            person.saveRecord(outputFile) 
            sleep(0.1) 

    def changePageNumber(self):
        self.page = self.page + 1
        self.pageNumber = "&PageNumber={}".format(str(self.page)) 
