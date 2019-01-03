from argparse import ArgumentParser 

class Arguments:
    def __init__(self):
        self.name = "" 
        self.location = "" 
        self.street = "" 
        self.outputFile = "" 

        self.parse() 

    def parse(self): 
        self.argumentParser = ArgumentParser()
        self.argumentParser.add_argument("-n", "--name", required=True,
                help="Surname of the Person")
        self.argumentParser.add_argument("-l", "--location", required=True,
                help="Location of the Person")
        self.argumentParser.add_argument("-o", "--output", required=True,
                help="Output file name(must be csv)")
        self.argumentParser.add_argument("-lim", "--limit", required=False,
                help="Number of contacts to fetch(Optional)")
        args = vars(self.argumentParser.parse_args()) 
        
        self.name = args["name"] 
        self.location = args["location"] 
        self.street = "" 
        self.outputFile = args["output"] 
