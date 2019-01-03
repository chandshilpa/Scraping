from Arguments import Arguments 
from CSVFile import CSVFile 
from scrape import Scraper

def main(name="", address="", output=""):
    if name =="":
        arguments = Arguments()
        outputFile = CSVFile(arguments.outputFile)
        scraper = Scraper(arguments.name, arguments.address, arguments.phone_no)
    else:
        outputFile = CSVFile(output)
        scraper =Scraper(name, address, "")
    done = False 
    while not done:
        try:
            scraper.getPage()
            scraper.parsePage()
            scraper.getPeopleInfo(outputFile)
            scraper.changePageNumber()
        except Exception as error:
            done = True 
            print("Done.") 
            print(error) 


if __name__ == "__main__": 
    main() 
