# A set of strings programming problems

import sys
import string
import operator

def getFisrtCharThatAppearsOnce(myString):
    """ Get the first char that appears once in the provided string.
    Only alphabetic chars are considered. """
    myString = "".join(myString.lower().split())
    charDict = {key:[0, 0] for key in string.ascii_lowercase}
    for pos, char in enumerate(myString):
        charDict[char][0] += 1
        charDict[char][1] = pos
    charDict = {key:values for key, values in charDict.items() if values[0] == 1}
    sortedCharDict = sorted(charDict.items(), key=operator.itemgetter(1))
    strOut = sortedCharDict[0][0] if sortedCharDict else False
    return strOut

if __name__ == "__main__":
    myString = "String to be tested"
    out = getFisrtCharThatAppearsOnce(myString)
    print(out)
