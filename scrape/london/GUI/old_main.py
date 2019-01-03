import urllib3 
import certifi 
from bs4 import BeautifulSoup 
import csv 
import argparse

http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        ) 

ap = argparse.ArgumentParser()
ap.add_argument("-sn", "--surname", required=True,
	help="Surname of the Person") 
ap.add_argument("-l", "--location", required=True,
        help="Location of the Person")
ap.add_argument("-o", "--output", required=True,
        help="Output file name(must be csv)") 
ap.add_argument("-lim", "--limit", required=False,
        help="Number of contacts to fetch(Optional)")
args = vars(ap.parse_args())

surname = args["surname"] 
location = args["location"] 
street = ""

csvfile = open(args["output"], "a") 
csvwriter = csv.writer(csvfile) 

url = "https://thephonebook.bt.com/Person/PersonSearch/?Surname={}&Location={}&Street={}".format(surname, location, street) 
page = http.request('GET', url) 
code = BeautifulSoup(page.data, 'html.parser') 

count = 0 

print()
print("+++++++++++++++")
print()

divs = code.find_all('div', class_="mb-3 border border-dark px-3")
for div in divs:
    rows = div.find_all('div', class_="row", recursive=False) 
    # For name
    row0span = rows[0].find('span', class_="black medium")
    name = row0span.text.strip() 
    print(name) 

    # For address 
    row1col8div = rows[1].find('div', class_="col-8 py-2") 
    address = row1col8div.text.strip()  
    print(address)

    # For Phone Number 
    phone = rows[2].find('div', class_="ml-3 d-inline light-blue my-auto no-wrap").text.strip() 
    print(phone) 

    print()
    print("+++++++++++++++")
    print() 

    csvrow = list() 
    csvrow.append(name) 
    csvrow.append(address) 
    csvrow.append(phone)

    csvwriter.writerow(csvrow) 


csvfile.close() 

