import re
import sys

class MyWordCounter():

    wordCounter = dict()
    inputFile   = ""
    outputFile  = ""

    def __init__(self):
        self.inputFile  = sys.argv[1]
        self.outputFile = sys.argv[2]
        print(self.inputFile)
        print(self.outputFile)

tester = MyWordCounter()