#This program analyzes a text file for certain key words and to determine certain statistics related to its contents. This data is then outputted to a csv file.
#by Daniel Moreno
#doesn't exactly fit requirements as Python doesn't allow unopened files to be passed as a parameter because no reference variables

#function to open and read file in output and input mode based on parameter
def readFile(file, fileName, isInput):
    file.close()
    try:
        if (isInput):
            file = open(fileName, "r")
        else:
            file = open(fileName, "w")
    except:
        print ("An error occurred while opening the file")

    return file

#function to parse the file and determine certain statistics of it
#it will take in the two files, output two arrays of lines for the file and the data for the console output, and the counter to track number of values in arrayOfText
def parser(fileOfNames,fileOfText,arrayOfText, numOfTextStats, textStats):
    #initialize variables
    numOfWords = 0
    numOfSentences = 1
    numOfParagraphs = 0
    numOfNamedEntitiesInArray = 0
    numOfNamedEntities = 0
    paragraphIndex = 1
    numOfWordsInEachParagraph = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    listOfNamedEntities = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    tempWord = ""
    lineToStore = ""
    tempLine = ""
    wordType = "word"
    changedSentence = False

    #store named entities from file in the array
    listOfLines = fileOfNames.readlines()
    i = 0
    for line in listOfLines:
        if ((line != "") and (line != "\n")):
            tempWord = ""
            for char in line :
                if (char != '\n') :
                    tempWord += char
            listOfNamedEntities[i] = tempWord
            i += 1
            
    #continually get lines from fileOfText
    linesList = fileOfText.readlines()
    for line in linesList:
        words = line.split()
        for word in words:
            #reset stuff
            wordType = "word"
            changedSentence = False
            #increase the word count
            numOfWords += 1

            #increase the sentence count and remove punctuation
            for char in word:
                   if (char == '.'):
                       changedSentence = True
                       numOfSentences += 1
            word = word.replace('.','')
            word = word.replace(',','')
            word = word.replace('(','')
            word = word.replace(')','')

            #check if it is a Named Entity
            for entry in listOfNamedEntities:
                if (entry == word):
                    wordType = "namedEntity"
                    numOfNamedEntities += 1

            #create the final string that will be written to the file
            #if the sentence count was increased because the word contained a period, don't display the increased number until the next word
            if (changedSentence):
                lineToStore = "w" + str(numOfWords) + ", p" + str(paragraphIndex) + ", s" + str(numOfSentences - 1) + ", " + wordType + ", " + word
            else:
                lineToStore = "w" + str(numOfWords) + ", p" + str(paragraphIndex) + ", s" + str(numOfSentences) + ", " + wordType + ", " + word
            arrayOfText[numOfTextStats] = lineToStore
            numOfTextStats += 1

        #get current paragraph number
        if (line != "\n"):
            paragraphIndex += 1
    #store text stats
    textStats[0] = numOfWords
    textStats[1] = numOfNamedEntities
    textStats[2] = numOfSentences - 1
    textStats[3] = paragraphIndex - 1

    return numOfNamedEntitiesInArray

#function to print the strings to the csv
#will take the file and the datas storage arrays as parameters
def writeFile(outputFile, arrayOfText, numOfTextStats,  textStats):
    #print stuff to file
    outputFile.write("words, paragraphs, sentences, type, word\n")
    for entry in arrayOfText:
        outputFile.write(entry + "\n")

    #print stuff to console
    print("Words: " + str(textStats[0]))
    print("Named Entities: " + str(textStats[1]))
    print("Sentences: " + str(textStats[2]))
    print("Paragraphs: " + str(textStats[3]))



#start execution here
#initialize variables
arrayOfText = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
numOfTextStats = 0
numOfNamedEntities = 0
textStats = [0,0,0,0]
bool1 = True
bool2 = False

#open files
try:
    namedEntitiesFile = open("named_entities.txt", "r")
    humanJabberFile = open("human_jabber.txt", "r")
    outputFile = open("output.csv", "w")
except:
    print ("An error occurred while opening the file")

#parse files
numOfNamedEntities = parser(namedEntitiesFile, humanJabberFile, arrayOfText, numOfTextStats, textStats)

#save everything
writeFile(outputFile, arrayOfText, numOfTextStats, textStats)