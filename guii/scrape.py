from bs4 import BeautifulSoup as Soup
from urllib3 import PoolManager
from urllib.request import urlopen as UReq
from certifi import where
from Person import Person
from time import sleep


class Scraper:
    def __init__(self, name, address,phone_no):
        self.http = PoolManager(
                    cert_reqs="CERT_REQUIRED",
                    ca_certs=where()
        )
        self.page = 1
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.url = format(self.page, name, address)

    def getPage(self):
        uClient = UReq(self.url)
        self.page_html = uClient.read()
        uClient.close()

    def parsePage(self):
        self.Soup = Soup(self.page_html, "html.parser")

    def getPeopleInfo(self, outputFile):

        divs = self.Soup.find_all("div", class_="c411Listing jsResultsList")
        if len(divs) == 0:
            raise Exception("No more records found. Total {} records found.".format(str(Person.totalPeople)))
        for div in divs:
            person = Person()
            val2 = div.find_all("div", class_ ="listing__row")
            val3 = div.find("h2", class_="c411ListedName")
            name = val3.find("a")
            person.setName(name.text.strip())

            phone_no = div.find("span", class_="c411Phone")
            person.setPhone(phone_no.text.strip())

            val1 = div.find_all("span", class_="c411ListingGeo")
            address = div.find("span", class_="adr")
            person.setAddress(address.text.strip())


            person.saveRecord(outputFile)
            sleep(0.1)

    def changePageNumber(self):
        self.page = self.page + 1
        self.url = "http://www.canada411.ca/search/si/{}/{}/{}/".format(self.page, self.name, self.address)




















