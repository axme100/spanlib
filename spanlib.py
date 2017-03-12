#Open Window Spanish Madlibs Project
#By: Max Carey

#To get random integers for the getRandomWord() function
from random import randint

#Google's Speech Syntensis
from gtts import gTTS

#For playing the audio files
#http://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python
import pygame

#For reading in the files
import os

#The first step is to read in the files as unicode (utf-8) using Python's 
#built-in open() statement to create a file object. Then use the files object's
#associated read() method to creat a list. splitlines() reads each line as an element in
#the list without importing line break characters.

#Open() is embedded in a with-as() statement, among other reasons, so that we don't
#have to close the file. See this website: #http://www.pythonforbeginners.com/files/with-statement-in-python

myDirectory = os.getcwd() + "/"

with open(myDirectory + 'kid_word_data/adj_o.txt', encoding="utf-8") as f:
    adj_o = f.read().splitlines()
        
with open(myDirectory + 'kid_word_data/adj_a.txt', encoding="utf-8") as f:
    adj_a = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_as.txt', encoding="utf-8") as f:
    adj_as = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_os.txt', encoding="utf-8") as f:
    adj_os = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_e.txt', encoding="utf-8") as f:
    adj_e = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_es.txt', encoding="utf-8") as f:
    adj_es = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_l.txt', encoding="utf-8") as f:
    adj_l = f.read().splitlines()

with open(myDirectory + 'kid_word_data/adj_les.txt', encoding="utf-8") as f:
    adj_les = f.read().splitlines()

#with open(myDirectory + 'kid_word_data/adj_n.txt', encoding="utf-8") as f:
#    adj_n = f.read().splitlines()

#with open(myDirectory + 'kid_word_data/adj_nes.txt', encoding="utf-8") as f:
#    adj_nes = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_o.txt', encoding="utf-8") as f:
    noun_o = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_os.txt', encoding="utf-8") as f:
    noun_os = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_a.txt', encoding="utf-8") as f:
    noun_a = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_as.txt', encoding="utf-8") as f:
    noun_as = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_e_fem.txt', encoding="utf-8") as f:
    noun_e_fem = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_es_fem.txt', encoding="utf-8") as f:
    noun_es_fem = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_e_masc.txt', encoding="utf-8") as f:
    noun_e_masc = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_es_masc.txt', encoding="utf-8") as f:
    noun_es_masc = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_dad.txt', encoding="utf-8") as f:
    noun_dad = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_dades.txt', encoding="utf-8") as f:
    noun_dades = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_ma.txt', encoding="utf-8") as f:
    noun_ma = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_mas.txt', encoding="utf-8") as f:
    noun_mas = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_tud.txt', encoding="utf-8") as f:
    noun_tud = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_tudes.txt', encoding="utf-8") as f:
    noun_tudes = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_cion.txt', encoding="utf-8") as f:
    noun_cion = f.read().splitlines()

with open(myDirectory + 'kid_word_data/noun_ciones.txt', encoding="utf-8") as f:
    noun_ciones = f.read().splitlines()

#Create empty lists that that have to be manually filled with word data (from )
fsaDict = []
fpaDict = []
msaDict = []
mpaDict = []
msnDict = []
mpnDict = []
fsnDict = []
fpnDict = []


#This function fills the word lists above, it should be called from the paragraph that students make
def setLists (one, two, three, four, five, six, seven, eight):
    global fsaDict, fpaDict, msaDict, mpaDict, msnDict, mpnDict, fsnDict, fpnDict
    fsaDict = one
    fpaDict = two
    msaDict = three
    mpaDict = four
    msnDict = five
    mpnDict = six
    fsnDict = seven
    fpnDict = eight

#Combine all of the lists that are imported from files to create an overall dictionary.
#dictionary = adj_o + adj_a + adj_as + adj_os + adj_e + adj_es + adj_l + adj_les + noun_a + noun_as + noun_dad + noun_dades + noun_e_fem + noun_es_fem + noun_e_masc + noun_es_masc + noun_tud + noun_tudes + noun_cion + noun_ciones

#Create possessive adjective dictionary without grammatical labeling
possAdjEasy = {
    "mi": ["mi"],
    "mis": ["mis"],
    "tu": ["tu"],
    "tus": ["tus"],
    "su": ["su"],
    "sus": ["sus"],
    "nuestro": ["nuestro"],
    "nuestros": ["nuestros"],
    "nuestra": ["nuestra"],
    "nuestras": ["nuestras"],
    "vuestro": ["vuestro"],
    "vuestros": ["mis"],
    "vuestra": ["vuestra"],
    "vuestras": ["mis"],
}

#With grammatical labels
possessiveAdj = {
    "1PS_SO": ["Mi"],
    "1PS_PO": ["Mis"],
    "2PS_SO": ["Tu"],
    "2PS_PO": ["Tus"],
    "3PS_SO": ["Su"],
    "3PS_PO": ["Sus"],
    "1PP_MSO": ["Nuestro"],
    "1PP_MPO": ["Nuestros"],
    "1PP_FSO": ["Nuestra"],
    "1PP_FSO": ["Nuestras"],
    "2PP_MSO": ["Vuestro"],
    "2PP_MPO": ["Vuestros"],
    "2PP_FSO": ["Vuestra"],
    "2PP_FPO": ["Vuestras"],
    "3PP_SO": ["Vuestras"],
    "3PP_PO": ["Vuestras"],
}


indirectObjectPronoun = {
    "1PS": ["me"],
    "2PS": ["te"],
    "3PS": ["le"],
    "1PP": ["nos"],
    "2PP": ["os"],
    "3PP": ["les"],
}

#Create a function that checks whether or not a given word is in the dictionary.
def checkDictionary(word):
    if (word in dictionary):
        return True
    else:
        return False

#This will display the instructions
def displayInstructions():
    print("")
    print("Bienvenidos al Spanish Mad-Libs")
    print("Vamos a jugar")
    print("")

#This method instructs the user to input a certain kind of adjective
def inputWord (wordType) :
    if (wordType == "msa"):
        message = "Dame un adjetivo masculino, singular: "
    elif (wordType== "mpa"):
        message = "Dame un adjetivo masculino, plural: "
    elif (wordType == "fsa"):
        message = "Dame un adjetivo feminino, singular: "
    elif (wordType == "fpa"):
        message = "Dame un adjetivo feminino, plural: "
    elif (wordType == "msn"):
        message = "Dame un sustantivo masculino, singular: "
    elif (wordType == "mpn"):
        message = "Dame un sustantivo masculino, plural: "
    elif (wordType == "fsn"):
        message = "Dame un sustantivo femenino, singular: "
    elif (wordType == "fpn"):
        message = "Dame un sustantivo femenino, plural: "

    #Note, to run python three the built-in function is just input() not raw_input
    #But this script does not work in python 2 if it is not raw_input()1    
    print("")
    word = input(message + "Al contrario, entra \"r\" para una palabra al azar (random): ")
    return word

def checkWord (wordType, word):
    warning = "Warning: Your adjective doesn't end in a regularly occuring suffix. "
    #If the adjective type is masculine singular
    #and the last letter is not o, regutrn false
    if ((wordType == "msa")
        and (word[-1]) != "o"
        and (word[-1]) != "e"
        and (word[-1]) != "l"
        and (word[-1]) != "n"):
            print("")
            print(warning + "Masculine singular adjectives regularly end in \"-o\", but also \"-e\" or \"-l\" or \"-n\"")
            print("")
            userChoice = input("Enter \"x\" to cancel and get a new word, or enter any other key to continue with this word anyway")
            if(userChoice == "x"):
                return False
    #If the adjective type is masculine plural
    #and the last letter is not o, return false
    elif ((wordType == "mpa")
        and (word[-2:]) != "os"
        and (word[-2:]) != "es"
        and (word[-2:]) != "les"
        and (word[-2:]) != "nes"):
            print("")
            print(warning + "Masculine plural adjectives regularly end in \"-os\", but also \"-es\" or \"-les\" or \"-nes\"")
            print("")
            userChoice = input("Enter \"x\" to cancel and get a new word, or enter any other key to continue with this word anyway")
            if(userChoice == "x"):
                return False
    #IF the adjective type is feminine singular
    #and the last letter is not -a, return false
    elif ((wordType == "fsa")
        and (word[-1]) != "a"
        and (word[-1]) != "e"
        and (word[-1]) != "l"
        and (word[-1]) != "n"):
            print("")
            print(warning + "Feminine singular adjectives regularly end in \"-a\", but also \"-e\" or \"-l\" or \"-n\"")
            print("")
            userChoice = input("Enter \"x\" to cancel and get a new word, or enter any other key to continue with this word anyway")
            if(userChoice == "x"):
                return False
    #IF the adjective is feminine plural
    #and the last lettera are not -as, return false
    elif ((wordType == "fpa")
        and (word[-2:]) != "as"
        and (word[-2:]) != "es"
        and (word[-2:]) != "les"
        and (word[-2:]) != "nes"):
            print("")
            print(warning + "Feminine Plural adjectives regularly end in \"-as\", but also \"-es\" or \"-les\" or \"-nes\"")
            print("")
            userChoice = input("Enter \"x\" to cancel and get a new word, or enter any other key to continue with this word anyway")
            if(userChoice == "x"):
                return False
    else:
        return True

def getRandomWord(wordType):
    randWord = ""
    randIndex = randint(0,199)
    if (wordType == "msa"):
        randWord = msaDict[randint(0, len(msaDict) - 1)]
    elif (wordType == "mpa"):
        randWord = mpaDict[randint(0, len(mpaDict) - 1)]
    elif (wordType == "fsa"):
        randWord = fsaDict[randint(0, len(fsaDict) - 1)]
    elif (wordType == "fpa"):
        randWord = fpaDict[randint(0, len(fpaDict) - 1)]
    elif (wordType == "msn"):
        randWord = msnDict[randint(0, len(msnDict) - 1)]
    elif (wordType == "mpn"):
        randWord = mpnDict[randint(0, len(mpnDict) - 1)]
    elif (wordType == "fsn"):
        randWord = fsnDict[randint(0, len(fsnDict) - 1)]
    elif (wordType == "fpn"):
        randWord = fpnDict[randint(0, len(fpnDict) - 1)]
            
    return randWord

def getMP3 (madLib):

    tts = gTTS(text=madLib, lang='es')
    tts.save("madlib.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("madlib.mp3")
    pygame.mixer.music.play()

def getWord (wordType):
    gotWord = False
    while (gotWord == False):
        myWord = inputWord(wordType)
        #If the user inserted the string "random"
        #Get a random word form the dictionary
        if (myWord == "r"):
            wordToAssign = getRandomWord(wordType)
            #I guess this will exit the loop, but I should
            #probably make it better.
            return wordToAssign
        else:
            #Otherwise, check to see if the word
            #ends in the right suffix
            gotWord = checkWord(wordType, myWord) #Here I would just add the function check in dictionary that would see if it's true. 
    return myWord