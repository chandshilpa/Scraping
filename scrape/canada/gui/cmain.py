from cArguments import Arguments
from CSVFile import CSVFile
from cScrape import Scraper


def cmain(name = "", location="", output=""):
    if name == "":
        arguments = Arguments()
        outputFile = CSVFile(arguments.outputFile)
        scraper = Scraper(arguments.name, arguments.location, arguments.phone_no)
    else:
        outputFile = CSVFile(output)
        scraper = Scraper(name, location , "")

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
    cmain()
