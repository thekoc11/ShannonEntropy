import math as mt
import sys as sy

f = open("files/allText.txt")
contents = f.read()
contents = contents.lower()
contents = contents.translate({ord(i): None for i in ';,.\n\"\'`()/-1234567890:–’‘&á%'})
joiningString = ''
alphabet = [' ']
for i in range(26):
    alphabet.append(chr(97 + i))


def incrementBlockSize(c):
    retArray = []
    for i in range(len(alphabet)):
        retArray.append(c + alphabet[i])
    return retArray


def dictByBlock(blockSize):
    sampleSpaceArray = []
    for j in range(len(alphabet)):
        sampleSpaceArray.append(alphabet[j])
    while len(list(sampleSpaceArray[len(sampleSpaceArray) - 1])) < blockSize:
        for i in range(len(sampleSpaceArray)):
            sampleSpaceArray[i] = incrementBlockSize(sampleSpaceArray[i])
        temp = []
        for i in range(len(sampleSpaceArray)):
            for j in range(len(sampleSpaceArray[i])):
                temp.append(sampleSpaceArray[i][j])
        sampleSpaceArray = temp
    retDict = {' ': 0}
    for i in range(len(sampleSpaceArray)):
        retDict[sampleSpaceArray[i]] = 0
    return retDict


def __main__():
    print(sy.getsizeof('a'))
    unigram = dictByBlock(1)
    unigram_prob = {'': 0.0}
    unigram_codeLength = {'': 0.0}
    entropy_Unigram = 0.0
    bigram = dictByBlock(2)
    bigram_prob = {'': 0.0}
    bigram_codeLength = {'':0.0}
    entropy_bigram = 0.0
    trigram = dictByBlock(3)
    trigram_prob = {'': 0.0}
    trigram_codeLength = {'':0.0}
    entropy_trigram = 0.0
    print(len(contents))
    for letter in contents:
        if letter in unigram:
            freq = unigram[letter]
            unigram[letter] = freq + 1
        # else:
        #     unigram.setdefault(letter, 1)

    print(unigram)
    unigram_prob.clear()
    for element in unigram:
        unigram_prob[element] = float(unigram[element] / len(contents))

    print(unigram_prob)

    _sum = 0.0
    sumN = 0
    unigram_codeLength.clear()
    for element in unigram_prob:
        _sum += unigram_prob[element]
        sumN += unigram[element]
        if unigram_prob[element] != 0.0:
            entropy_Unigram += unigram_prob[element] * mt.log2(1 / unigram_prob[element])
            unigram_codeLength[element] = mt.ceil(mt.log2(1/unigram_prob[element]))

    l_av = 0.0
    for element in unigram_codeLength:
        l_av += unigram_prob[element]*unigram_codeLength[element]
    print(unigram_codeLength)
    print(_sum, sumN, entropy_Unigram, l_av, l_av*len(contents)/8)

    for i in range(len(contents)):
        if i + 1 != len(contents):
            bigramString = joiningString.join([contents[i], contents[i + 1]])
            if bigramString in bigram:
                freq = bigram[bigramString]
                bigram[bigramString] = freq + 1

    print(bigram)
    sumN = 0
    for element in bigram:
        sumN += bigram[element]

    print(sumN)
    bigram_prob.clear()
    for element in bigram:
        bigram_prob[element] = float(bigram[element] / sumN)
    print(bigram_prob)
    _sum = 0.0
    bigram_codeLength.clear()
    for element in bigram_prob:
        _sum += bigram_prob[element]
        if bigram_prob[element] != 0.0:
            entropy_bigram += bigram_prob[element] * mt.log2(1 / bigram_prob[element])
            bigram_codeLength[element] = mt.ceil(mt.log2(1 / bigram_prob[element]))
    print(bigram_codeLength)
    l_av = 0.0
    for element in bigram_codeLength:
        l_av += bigram_prob[element] * bigram_codeLength[element]
    print(_sum, entropy_bigram, l_av)

    for i in range(len(contents)):
        if i + 2 < len(contents):
            trigramString = joiningString.join([contents[i], contents[i + 1], contents[i+2]])
            if trigramString in trigram:
                freq = trigram[trigramString]
                trigram[trigramString] = freq + 1

    print(trigram)
    sumN = 0
    for element in trigram:
        sumN += trigram[element]

    print(sumN)
    trigram_prob.clear()
    for element in trigram:
        trigram_prob[element] = float(trigram[element] / sumN)
    print(trigram_prob)
    _sum = 0.0
    for element in trigram_prob:
        _sum += trigram_prob[element]
        if trigram_prob[element] != 0.0:
            entropy_trigram += trigram_prob[element] * mt.log2(1 / trigram_prob[element])
    print(_sum, entropy_trigram)


__main__()
