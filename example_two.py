import spanlib

#Creat subdictionaries for
#For getting ranodm words
fsaDict = spanlib.adj_a + spanlib.adj_e + spanlib.adj_l
fpaDict = spanlib.adj_as + spanlib.adj_es + spanlib.adj_les
msaDict = spanlib.adj_o + spanlib.adj_e + spanlib.adj_l
mpaDict = spanlib.adj_os + spanlib.adj_es + spanlib.adj_les

msnDict = spanlib.noun_o + spanlib.noun_e_masc
mpnDict = spanlib.noun_os + spanlib.noun_es_masc
fsnDict = spanlib.noun_a + spanlib.noun_e_fem + spanlib.noun_dad + spanlib.noun_ma + spanlib.noun_tud + spanlib.noun_cion
fpnDict = spanlib.noun_as + spanlib.noun_es_fem + spanlib.noun_dades + spanlib.noun_mas + spanlib.noun_tudes + spanlib.noun_ciones

spanlib.setLists(fsaDict, fpaDict, msaDict, mpaDict, msnDict, mpnDict, fsnDict, fpnDict)


hacer = {
    "1PS": ["hago"],
    "2PS": ["haces"],
    "3PS": ["hace"],
    "1PP": ["hacemos"],
    "2PP": ["hacéis"],
    "3PP": ["hacen"],
}

conversar = {
    "1PS": ["converso"],
    "2PS": ["conversas"],
    "3PS": ["conversa"],
    "1PP": ["conversamos"],
    "2PP": ["conversáis"],
    "3PP": ["conversan"],
}

def myExample(subject, possAdj):
    pa = spanlib.possessiveAdj[possAdj][0]
    verbOne = hacer[subject][0]
    verbTwo = conversar[subject][0]
    adjOne = spanlib.getWord("msa")
    adjTwo = spanlib.getWord("fsa")
    adjThree = spanlib.getWord("fpa")
    adjFour = spanlib.getWord("mpa")
    adjFive = spanlib.getWord("fsa")
    nounOne = spanlib.getWord("mpn")
    nounTwo = spanlib.getWord("mpn")
    nounThree = spanlib.getWord("fpn")
    #         #pa,                                                  verb1,          adjOne, pa,                         adjTwo,                                                             adjThree, verbTwo,              adjFour,  nounOne,  nounTwo,  nounThree, adjFive, pa               
    madlib = ("{} nombre es Max. Por la mañana, la primera cosa que {} es tomar café {} con {} mejor amiga quien es muy {}. Sin embargo, a ella no le gusta el café y perfiere tomar bebidas {}. {} muchas horas sobre temas {} como los {}, los {}, y las {}. Qué {} es {} vida".format(pa,verbOne,adjOne,pa,adjTwo,adjThree,verbTwo,adjFour,nounOne,nounTwo,nounThree,adjFive,pa))
    print("")
    print(madlib)
    print("")
    spanlib.getMP3(madlib)

myExample("1PS","1PS_SO")
myExample("2PS","2PS_SO") #Check why the audio doesn't play on this function call.