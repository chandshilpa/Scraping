from csv import (
            writer,
        )

class CSVFile:
    def __init__(self, filename):
        self.file = open(filename, 'a')
        self.writer = writer(self.file)

    def appendRow(self, row):
        self.writer.writerow(row)

    def __del__(self):
        self.file.close()
