#alex ortega
import re
import sys

class MyWordCounter():

    wordCounter = dict()
    inputFile   = ""
    outputFile  = ""

    def __init__(self):
        self.inputFile  = sys.argv[1]
        self.outputFile = sys.argv[2]
        self._readWords()

    def _readWords(self):
        #each line will be formatted and stored into the dictionary
        file = open(self.inputFile, "r")
        for line in file:
            line = line.strip()
            line = line.lower()
            wordsInLine = line.split()

            for word in wordsInLine:
                #strip all non-alpha characters from the word
                word = re.sub('[^A-Za-z0-9]+', '', word)

                #check if word is in dictionary, if not then add it
                if word in self.wordCounter:
                    self.wordCounter[word] += 1
                else:
                    self.wordCounter[word] = 1
        self._writeWords()

    def _writeWords(self):
        #will create file and write count and words from dictionary
        output = open(self.outputFile, "w")
        output.write("Count:\tWord:\n")
        for x in sorted(self.wordCounter):
            wordString = str(self.wordCounter[x])+":\t "+str(x)
            #write word in the output file
            output.write(wordString)
            output.write("\n")
        output.close()
        print("Done. Output file is in your directory. Thank you. ")

tester = MyWordCounter()