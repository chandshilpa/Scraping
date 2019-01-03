from argparse import ArgumentParser 

class Arguments:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone_no = ""
        self.outputFile = "" 

        self.parse()



    def parse(self): 
        self.argumentParser = ArgumentParser()
        self.argumentParser.add_argument("-n", "--name", required=True,
                help="name of the Person")
        self.argumentParser.add_argument("-l", "--address", required=True,
                help="address of the Person")
        self.argumentParser.add_argument("-o", "--output", required=True,
                help="Output file name(must be csv)")
        self.argumentParser.add_argument("-lim", "--limit", required=False,
                help="Number of contacts to fetch(Optional)")
        args = vars(self.argumentParser.parse_args())
        
        self.name = args["name"]
        self.address = args["address"]
        self.phone_no = ""
        self.outputFile = args["output"]


