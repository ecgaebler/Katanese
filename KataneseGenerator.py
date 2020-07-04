from syllable_frequencies import *
from GrammarDict import *
import random
import io
import sys

#Parse syllable frequencies and construct weighted random number generator
syllable_list = []
weights = []
marks = []
#unpack syllables and their weights
for syllable, weight in syllable_weights:
    if weight > 0:
        syllable_list.append(syllable)
        weights.append(weight)
#calculate marks for random number generator based on syllable weights
if len(weights) > 0:
    marks = [weights[0]]
    for i in range(1,len(weights)):
        #Each mark corresponds to the sum of all weights before the current syllable weight
        marks.append(marks[i - 1] + weights[i])

def err(string):
    print(string, file=sys.stderr)
    return

def line():
    print("-" * 80)

def closest_mark(nums, target):
    """ Returns index of closest value not less than target. """
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l)//2
        if nums[mid] < target:
            l = mid
        else:
            r = mid
    if nums[l] >= target:
        return l
    else:
        return r

def new_syllable(syllables, excluded=[]):
    """ Returns a random syllable.
    INPUTS:
    syllables —— a list of syllables to select from
    excluded —— a list of syllables to exclude
    """
    if not syllables or syllables == excluded:
        err("UM: NO VALID SYLLABLES SUPPLIED")
        return ""
    while True:
        target = random.randint(0,marks[-1])
        # Find index of closest mark such that target <= mark
        mark = closest_mark(marks, target)
        if syllables[mark] not in excluded:
            break
    return syllables[mark]


def newSyllable(vowels=True, nr=True, others=True):
    """ if 'vowels', allow vowels. 'nr' allows n/r. 'others' is for all else.
    Returns a random syllable, weighted on the probability of each
    """
    cycle = True;
    syllable = ""
    while (cycle):
        sylnum = random.randint(1,mark_hjo)
        if sylnum <= mark_a : syllable = 'a'
        elif sylnum <= mark_i : syllable = 'i'
        elif sylnum <= mark_u : syllable = 'u'
        elif sylnum <= mark_e : syllable = 'e'
        elif sylnum <= mark_o : syllable = 'o'
        elif sylnum <= mark_n : syllable = 'n'
        elif sylnum <= mark_r : syllable = 'r'
        elif sylnum <= mark_pa : syllable = 'pa'
        elif sylnum <= mark_pi : syllable = 'pi'
        elif sylnum <= mark_pu : syllable = 'pu'
        elif sylnum <= mark_pe : syllable = 'pe'
        elif sylnum <= mark_po : syllable = 'po'
        elif sylnum <= mark_ba : syllable = 'ba'
        elif sylnum <= mark_bi : syllable = 'bi'
        elif sylnum <= mark_bu : syllable = 'bu'
        elif sylnum <= mark_be : syllable = 'be'
        elif sylnum <= mark_bo : syllable = 'bo'
        elif sylnum <= mark_ma : syllable = 'ma'
        elif sylnum <= mark_mi : syllable = 'mi'
        elif sylnum <= mark_mu : syllable = 'mu'
        elif sylnum <= mark_me : syllable = 'me'
        elif sylnum <= mark_mo : syllable = 'mo'
        elif sylnum <= mark_ta : syllable = 'ta'
        elif sylnum <= mark_ti : syllable = 'chi'
        elif sylnum <= mark_tu : syllable = 'tsu'
        elif sylnum <= mark_te : syllable = 'te'
        elif sylnum <= mark_to : syllable = 'to'
        elif sylnum <= mark_da : syllable = 'da'
        elif sylnum <= mark_di : syllable = 'di'
        elif sylnum <= mark_du : syllable = 'du'
        elif sylnum <= mark_de : syllable = 'de'
        elif sylnum <= mark_do : syllable = 'do'
        elif sylnum <= mark_na : syllable = 'na'
        elif sylnum <= mark_ni : syllable = 'ni'
        elif sylnum <= mark_nu : syllable = 'nu'
        elif sylnum <= mark_ne : syllable = 'ne'
        elif sylnum <= mark_no : syllable = 'no'
        elif sylnum <= mark_ra : syllable = 'ra'
        elif sylnum <= mark_ri : syllable = 'ri'
        elif sylnum <= mark_ru : syllable = 'ru'
        elif sylnum <= mark_re : syllable = 're'
        elif sylnum <= mark_ro : syllable = 'ro'
        elif sylnum <= mark_sa : syllable = 'sa'
        elif sylnum <= mark_si : syllable = 'shi'
        elif sylnum <= mark_su : syllable = 'su'
        elif sylnum <= mark_se : syllable = 'se'
        elif sylnum <= mark_so : syllable = 'so'
        elif sylnum <= mark_za : syllable = 'za'
        elif sylnum <= mark_zi : syllable = 'zi'
        elif sylnum <= mark_zu : syllable = 'zu'
        elif sylnum <= mark_ze : syllable = 'ze'
        elif sylnum <= mark_zo : syllable = 'zo'
        elif sylnum <= mark_ja : syllable = 'ya'
        elif sylnum <= mark_ji : syllable = 'yi'
        elif sylnum <= mark_ju : syllable = 'yu'
        elif sylnum <= mark_je : syllable = 'ye'
        elif sylnum <= mark_jo : syllable = 'yo'
        elif sylnum <= mark_ka : syllable = 'ka'
        elif sylnum <= mark_ki : syllable = 'ki'
        elif sylnum <= mark_ku : syllable = 'ku'
        elif sylnum <= mark_ke : syllable = 'ke'
        elif sylnum <= mark_ko : syllable = 'ko'
        elif sylnum <= mark_ga : syllable = 'ga'
        elif sylnum <= mark_gi : syllable = 'gi'
        elif sylnum <= mark_gu : syllable = 'gu'
        elif sylnum <= mark_ge : syllable = 'ge'
        elif sylnum <= mark_go : syllable = 'go'
        elif sylnum <= mark_wa : syllable = 'wa'
        elif sylnum <= mark_wi : syllable = 'wi'
        elif sylnum <= mark_wu : syllable = 'wu'
        elif sylnum <= mark_we : syllable = 'we'
        elif sylnum <= mark_wo : syllable = 'wo'
        elif sylnum <= mark_ha : syllable = 'ha'
        elif sylnum <= mark_hi : syllable = 'hi'
        elif sylnum <= mark_hu : syllable = 'fu'
        elif sylnum <= mark_he : syllable = 'he'
        elif sylnum <= mark_ho : syllable = 'ho'
        elif sylnum <= mark_pja : syllable = 'pya'
        elif sylnum <= mark_pji : syllable = 'pyi'
        elif sylnum <= mark_pju : syllable = 'pyu'
        elif sylnum <= mark_pje : syllable = 'pye'
        elif sylnum <= mark_pjo : syllable = 'pyo'
        elif sylnum <= mark_bja : syllable = 'bya'
        elif sylnum <= mark_bji : syllable = 'byi'
        elif sylnum <= mark_bju : syllable = 'byu'
        elif sylnum <= mark_bje : syllable = 'bye'
        elif sylnum <= mark_bjo : syllable = 'byo'
        elif sylnum <= mark_mja : syllable = 'mya'
        elif sylnum <= mark_mji : syllable = 'myi'
        elif sylnum <= mark_mju : syllable = 'myu'
        elif sylnum <= mark_mje : syllable = 'mye'
        elif sylnum <= mark_mjo : syllable = 'myo'
        elif sylnum <= mark_tja : syllable = 'tya'
        elif sylnum <= mark_tji : syllable = 'tyi'
        elif sylnum <= mark_tju : syllable = 'tyu'
        elif sylnum <= mark_tje : syllable = 'tye'
        elif sylnum <= mark_tjo : syllable = 'tyo'
        elif sylnum <= mark_nja : syllable = 'nya'
        elif sylnum <= mark_nji : syllable = 'nyi'
        elif sylnum <= mark_nju : syllable = 'nyu'
        elif sylnum <= mark_nje : syllable = 'nye'
        elif sylnum <= mark_njo : syllable = 'nyo'
        elif sylnum <= mark_rja : syllable = 'rya'
        elif sylnum <= mark_rji : syllable = 'ryi'
        elif sylnum <= mark_rju : syllable = 'ryu'
        elif sylnum <= mark_rje : syllable = 'rye'
        elif sylnum <= mark_rjo : syllable = 'ryo'
        elif sylnum <= mark_sja : syllable = 'sya'
        elif sylnum <= mark_sji : syllable = 'syi'
        elif sylnum <= mark_sju : syllable = 'syu'
        elif sylnum <= mark_sje : syllable = 'sye'
        elif sylnum <= mark_sjo : syllable = 'syo'
        elif sylnum <= mark_zja : syllable = 'zya'
        elif sylnum <= mark_zji : syllable = 'zyi'
        elif sylnum <= mark_zju : syllable = 'zyu'
        elif sylnum <= mark_zje : syllable = 'zye'
        elif sylnum <= mark_zjo : syllable = 'zyo'
        elif sylnum <= mark_kja : syllable = 'kya'
        elif sylnum <= mark_kji : syllable = 'kyi'
        elif sylnum <= mark_kju : syllable = 'kyu'
        elif sylnum <= mark_kje : syllable = 'kye'
        elif sylnum <= mark_kjo : syllable = 'kyo'
        elif sylnum <= mark_gja : syllable = 'gya'
        elif sylnum <= mark_gji : syllable = 'gyi'
        elif sylnum <= mark_gju : syllable = 'gyu'
        elif sylnum <= mark_gje : syllable = 'gye'
        elif sylnum <= mark_gjo : syllable = 'gyo'
        elif sylnum <= mark_hja : syllable = 'hya'
        elif sylnum <= mark_hji : syllable = 'hyi'
        elif sylnum <= mark_hju : syllable = 'hyu'
        elif sylnum <= mark_hje : syllable = 'hye'
        elif sylnum <= mark_hjo : syllable = 'hyo'
        else : syllable = 'quo'
        if (syllable in ['a','i','u','e','o'] and not vowels):
            cycle = True    #generate the syllable over again
        elif (syllable in ['n','r'] and not nr):
            cycle = True
        else:
            if not others:
                cycle = True
            else:
                cycle = False
    return syllable


def syllables(s=2):
    """ Return a word composed of s concatenated random syllables. 
    This function includes the phonetic rules for the language being created.
    Until modified, these rules are designed to generate words with phonetic
    structure almost identical to those of Japanese words. If you want complex
    phonetic rules, this function is where they should be defined.
    """
    word = ""
    vowels = True
    nr = False  # Initial syllable cannot be 'n' or 'r'
    others = True
    
    if s == 0:
        return ""

    if s == 1:
        vowels = False
        #return newSyllable(vowels,nr,others)
        return new_syllable(syllable_list, ["n", "r"])

    #TODO: rewrite this structure to use newer new_syllable function
    if s > 1:
        newSyl = ""
        for i in range(s):
            if i == 0 or 1 == s:
                nr = False      # Word cannot start or end in 'n' or 'r'
            newSyl = newSyllable(vowels,nr,others)
            #newSyl = new_syllable(syllable_list, ["n", "r"])
            if newSyl in ['n','r']:
                vowels = False  # Vowel cannot follow isolated 'n' or 'r'
                nr = False      # Double 'n' or 'r' not allowed
                others = True
            elif newSyl in ['a','i','u','e','o']:
                vowels = False  # Double isolated vowels not allowed
                nr = True
                others = True
            else:
                vowels = True
                nr = True
                others = True    
            word = word + newSyl
        return word

    else:
        err("[YOU DONE MESSED UP: INVALID NUMBER OF SYLLABLES]")
        return ""

'''
# UNUSED FUNCTIONS
def doubleWord(s):
    """ Return the first s-syllable word generated simultaneously by two generators.
    This amplifies the effects of the weights given to different syllables, 
    making common syllables even more common, and rare syllables even more rare.
    """
    word1 = syllables(s)
    word2 = syllables(s)
    while word1 != word2:
        word1 = syllables(s)
        word2 = syllables(s)
    return word1

def wordsSquared(n,s):
    """ return n s-syllable words using doubleWord to amplify probabilities """
    words = ""
    for i in range(1,n):
        word = doubleWord(s)
        while word in words:
             word = doubleWord(s)
        words = words + " " + word
    return words

def words(n,s=1):
    """ return n distinct words, each with s syllables """
    words = ""
    for i in range(1,n):
        word = syllables(s)
        while word in words:
             word = syllables(s)
        words = words + " " + word
    return words
'''

def file_to_wordlist(path='./wordlist_Nsyllable'):
    """ Return lists of simple and complex words found in file at given path.
    Input defaults to "wordlist_Nsyllable" file.
    """
    print("parsing file...")
    inFile = open(path).read()
    wordList = []
    compoundList = []
    word = ""
    compWord = False
    
    for c in inFile:
        if c != " ":
            if c == "," or c == "\n":   # ',' and '\n' mark the end of a word
                if word != "":
                    if not compWord:    # Simple word
                        if not word in wordList:
                            wordList += [word]
                    else:               # Compond word
                        if not word in compoundList:
                            compoundList += [word]
                word = ""
            elif c == "[":  # '[' marks the beginning of a compound word
                if not compWord:
                    compWord = True
                    inBrackets = True
                else:
                    err("YOU DONE GOOFED: DOUBLE '[' IN FILE")
                    return [wordList,compoundList]
            elif c == "]":
                if compWord:
                    compoundList += [word]
                    word = ""
                    compWord = False
                else:
                    err("YOU DONE IT WRONG: UNMATCHED ']' IN FILE")
                    return [wordList,compoundList]
            else: 
                word += c
    print("file parsing complete.")
    line()
    return [wordList,compoundList]


def parseCompWord(compWord):
    """ parse a compound word, returning a list of its component words """
    readingComp = False # Are the pieces of a compound word being read?
    compWordParse = []  # This will contain a list of compWord's component words
    currentWord = ""    # Word currently being built

    for c in compWord:
        if c in ["[","]"," ","\n"]:
            err("YEAH NO: YOU'RE NOT ACTUALLY READING FROM A FILE, ARE YOU?")
        elif c == "(":
            if not readingComp:
                compWordParse += [currentWord]
                currentWord = ""
                readingComp = True
            else:
                err("GRATZ. YOU MESSED UP: EXPECTED WORD BEFORE '('")
                return wordList
        elif c == "+":
            if not readingComp:
                err("NAH, BRUH, NAH: '+' FOUND OUTSIDE PARENTHESES")
            else:
                if currentWord == "":
                    err("YEAH NO: CANNOT PARSE NULL COMPOUND WORD")
                else:
                    compWordParse += [currentWord]
                    currentWord = ""
        elif c == ")":
            if not readingComp:
                err("SORRY: UNMATCHED ')' IN WORD")
            else:
                readingComp = False
                compWordParse += [currentWord]
                currentWord = ""
        else:
            currentWord += c

    if readingComp:
        err("SORRY DUDE(ETTE): UNMATCHED '('")
    return compWordParse

'''
def generateWordsDict(wordLists=[[],[]],
                      D={},
                      prob1=9,
                      prob2=80,
                      prob3=10,
                      prob4=1):
'''
def generateWordsDict(simple_words, compound_words, existing_dict, weights=[9,80,10,2,1]):
    """ Generate translations for compund and simple words. 

    INPUTS:
    simple_words —— a list strings representing simple words

    compound_words —— a list strings representing compound words

    existing_dict —— a dictionary of existing words and their translations,
                     to be added to as new translations are generated.

    weights —— a list of weights for the number of syllables. A heigher weight
               means a higher probability of being chosen. The weight at index 
               i corresponds to the chance of the word having i syllables.
    """
    print("beginning translation...")
    existing_words = list(existing_dict.values())
    new_word = ""   # This is the current word being processed
    compWord = []   # This will contain, in order, the pieces of a compound
    parsedWord = "" # This holds a compound word after parsing
    wordsTranslated = ""    # This will hold a list of all words added
    
    weight_sum = sum(weights)
    if weight_sum == 0:
        err("YOU DONE IT WRONG: INVALID PROBABILITY DISTRIBUTION")
        return []

    randomNum = 0
    skipping = False #"skipping" is only used for the explanatory printing 

    # Generate translations for simple words
    print("...generating simple word translations")
    for word in simple_words:
        new_word = ""
        # Make sure key doesn't already exist
        if word in existing_dict:
            skipping = True
        else:
            # Make sure value doesn't already exist
            while (new_word == "" or new_word in existing_words):
                randomNum = random.choice(list(range(weight_sum))) + 1
                if randomNum <= prob1:
                    new_word = syllables(1)
                elif randomNum <= prob1 + prob2:
                    new_word = syllables(2)
                elif randomNum <= prob1 + prob2 + prob3:
                    new_word = syllables(3)
                else:
                    new_word = syllables(4)
            existing_dict[word] = new_word
            wordsTranslated += "\n" + word + ": " + new_word
    if skipping:
        print("...Skipping words already defined")
        skipping = False

    # Generate translations for compound words. 
    # Note that all components of a compound word must already be defined.
    print("...generating compound word translations")
    for word in compound_words:
        new_word = ""
        parsedWord = parseCompWord(word)
        # Make sure key doesn't already exist
        if parsedWord[0] in existing_dict:
            skipping = True
        else:
            if len(parsedWord) < 2:
                err("NO CAN DO: 'COMPOUND WORD' EITHER BROKEN OR NOT COMPOUND")
                err("BROKEN WORD: " + word)
                return existing_dict
            else:
                #print("-  word components: ", parsedWord[1:])
                for piece in parsedWord[1:]:
                    if piece not in existing_dict:
                        err("OOPS: COMPONENT OF COMPOUND WORD NOT YET DEFINED")
                        err("BROKEN WORD: " + word)
                        err("MISSING WORD: " + piece)
                        return existing_dict
                    else:
                        # Build new word from words already found in dictionary
                        new_word += existing_dict[piece]
            if not parsedWord[0] in existing_dict:
                existing_dict[parsedWord[0]] = new_word
                wordsTranslated += "\n" + parsedWord[0] + ": " + new_word
            else:
                err("NOPE: COMPOUND WORD COLLISION")
                err("tried to change " + parsedWord[0] +
                    " from " + existing_dict[parsedWord[0]] +
                    " to " + new_word)
    if skipping:
        print("...Skipping compound words already defined")

    print("translation complete.")
    if not wordsTranslated == "":
        print("new translations: " + wordsTranslated[:-2])
    else:
        print("no new words.")
    line()
    return existing_dict


def printDict(D={}):
    """ Print out a dictionary in a nice format """
    translateList = []
    translation = ""
    for key in D:
        translation = key + ": " + D[key]
        translateList += [translation]
    translateList.sort()
    printOut = ""
    for word in translateList:
        printOut += word + "\n"
    print(printOut)
    return


def createKatanese():
    """ Generate all translations from English to Katanese """
    wordlist_1syl = file_to_wordlist('./wordlist_1syllable')
    wordlist_Nsyl  = file_to_wordlist('./wordlist_Nsyllable')
    D = grammarDict
    dict_1syl = generateWordsDict(wordlist_1syl, D, 1, 0, 0, 0)
    for key in dict_1syl:
        D[key] = dict_1syl[key]
    dict_Nsyl = generateWordsDict(wordlist_Nsyl, D)
    for key in dict_Nsyl:
        D[key] = dict_Nsyl[key]
    printDict(D)
    return

def addWords(new_words_path='./additional_words',
             prob1=19,
             prob2=1,
             prob3=0,
             prob4=0):
    """ Add words to an existing translation dictionary.

    ARGUMENTS:
    new_words_path —— file path to file containing a list of words to add
    prob1 ... prob4 —— probability weights for any new word having 1 ... 4 syllables

    """
    dict_path = './existing_dictionary'
    D = listToDict(readTranslations(dict_path))
    new_words = file_to_wordlist(new_words_path)
    D = generateWordsDict(new_words, D, 9, 80, 10, 1)
    printDict(D)
    return


def readTranslations(path='./existing_dictionary'):
    """ Read an existing dictionary file and parse it into a list """
    lines = open(path).readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]  # Remove newline characters
    return lines


def listToDict(L=[]):
    """ Convert a list of translations into a dictionary """
    copyingKey = True
    key = ""
    value = ""
    D = {}
    for line in L:
        copyingKey = True
        for c in line:
            if c == ':' or c == ' ':
                copyingKey = False
            elif copyingKey:
                key += c
            else:
                value += c
        D[key] = value
        key = ""
        value = ""
    return D
    
