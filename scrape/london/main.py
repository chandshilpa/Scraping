from Arguments import Arguments 
from CSVFile import CSVFile 
from Scraper import Scraper 

def main(surname="", location="", output=""):
    if surname == "":
        arguments = Arguments()
        outputFile = CSVFile(arguments.outputFile)
        scraper = Scraper(arguments.name, arguments.location, arguments.street)
    else:
        outputFile = CSVFile(output)
        scraper = Scraper(surname, location, "")
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
