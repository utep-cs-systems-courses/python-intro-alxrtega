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

    def printWords(self):
        #each line will be formatted and stored into the dictionary
        file = open(self.inputFile, "r")
        for line in file:
            line = line.strip()
            line = line.lower()
            wordsInLine = line.split(" ")

            for word in wordsInLine:
                #strip all non-alpha characters from the word
                word = re.sub('[^A-Za-z0-9]+', '', word)

                #check if word is in dictionary, if not then add it
                if word in self.wordCounter:
                    self.wordCounter[word] += 1
                else:
                    self.wordCounter[word] = 1

tester = MyWordCounter()
tester.printWords()