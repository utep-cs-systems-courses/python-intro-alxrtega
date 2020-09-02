#alex ortega
import re, sys, os

class MyWordCounter():

    wordCounter = dict()
    inputFile   = ""
    outputFile  = ""

    def __init__(self):
        if len(sys.argv) != 3:
            print("***Correct usage: python MyWordCounter.py <input text file> <output text file>***")
            exit()

        self.inputFile  = sys.argv[1]
        self.outputFile = sys.argv[2]

        if not self.outputFile.endswith('.txt'):
            print("***Output file %s should be a .txt file.***" % self.outputFile)
            exit()

        if not os.path.exists(self.inputFile):
            print ("***Input file %s doesn't exist.***" % self.inputFile)
            exit()

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

                #checking if word is in dictionary, if not then add it
                if word in self.wordCounter:
                    self.wordCounter[word] += 1
                else:
                    self.wordCounter[word] = 1
        self._writeWords()

    def _writeWords(self):
        #will create file and write count and sorted words from dictionary
        output = open(self.outputFile, "w")
        output.write("Count:\tWord:\n")
        for x in sorted(self.wordCounter):
            wordString = str(self.wordCounter[x])+":\t "+str(x)
            output.write(wordString)
            output.write("\n")
        output.close()
        print("Done. Output file is in your directory. Thank you.\n")

tester = MyWordCounter()