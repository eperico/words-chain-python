import sys

def setupDictionary(words) :
    upperWords = list()
    for word in words :
        upperWords.append(word.upper().strip('\n'))
    return tuple(upperWords)

def allNeighbourWords(word) :
    neighbours = set()
    # for every letter
    wordLength = len(word)
    for letter in range(0, wordLength) :
        splitWord = list(word)
        # change this letter to something else
        for c in range(ord('A'), ord('Z') + 1) :
            alphaCaracter = chr(c)
            if alphaCaracter != word[letter] :
                splitWord[letter] = alphaCaracter
                neighbours.add("".join(splitWord))
    return neighbours

def findWordsChain(startWord, stopWord, dictionary) :
    startWord, stopWord = startWord.upper(), stopWord.upper()
    chain = list()
    visitedWords = set()
    backtrack = dict()

    chain.append(startWord)
    visitedWords.add(startWord)

    while len(chain) > 0 :
        firstWord = chain.pop(0)
        # for each neighbour of first word
        for neighbour in allNeighbourWords(firstWord) :
            if neighbour == stopWord :
                # word found, backtrack
                pruneChain = [neighbour]
                while len(firstWord) > 0 :
                    pruneChain.insert(0, firstWord)
                    if firstWord in backtrack :
                        firstWord = backtrack[firstWord]
                    else :
                        firstWord = ""
                return pruneChain

            if neighbour in dictionary :
                if not neighbour in visitedWords :
                    chain.append(neighbour)
                    # mark visited
                    visitedWords.add(neighbour)
                    backtrack[neighbour] = firstWord

# Run
try:
    fileName = sys.argv[1]
except IndexError:
    print("Error: No input file")
else:
    file = open(fileName,"r")
    words = file.readlines()
    file.close()
    dictionary = setupDictionary(words)

    # test with simple dictionary
    wordschain = findWordsChain("tree", "flat", dictionary)

    # test with unix words
    # wordschain = findWordsChain("cat", "dog", dictionary)

    print(wordschain)
