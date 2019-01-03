from Arguments import Arguments 
from CSVFile import CSVFile 
from Scraper import Scraper 

def main(): 
    arguments = Arguments()
    outputFile = CSVFile(arguments.outputFile) 
    scraper = Scraper(arguments.name, arguments.location, arguments.street) 
    
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
