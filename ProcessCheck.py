import re

logStrings=["abcdeabcde", "abacdebcde", "abcdeabcce", "abcdeabcd", "ababcdcee", "aaabbbcccdddeee", "aaabcdebcdebcde"]

def firstEntryCheck():
    """ The first letter in a logString has to be 'a'. """

def LastEntryCheck():
    """ The first letter in a logString has to be 'e', Otherwise the process can not be complete """

def LenEntryCheck():
    """ The length of the logString has to be a multiple of 5, otherwise not all processes finished."""

# read logStrings, string by string
example=1
for logString in logStrings:
    print()
    print('Example: ', example)
    logStringLen = len(logString)
    if logString[0] != 'a':
        print('ERROR:logString does not start with an "a"')
        print(logString, '-1')
    if logString[logStringLen-1] != 'e':
        print('ERROR:logString does not end with an "e"')
        print(logString, '-1')
    elif logStringLen % 5 != 0:
        print("ERROR:logString does not have a multiple of 5 results")
        print(logString, '-1')
    else:
        print(logString)
        #results=[]
        results=''
        OutOfSequence=False
        for logChar in logString:
            print("Processing: ", logChar)
            if logChar == 'a':
                if 'e' in results:
                    #print("reuse e")
                    results = results.replace('e', 'a', 1)
                else:
                    #results.append('a')
                    results+='a'
            if logChar == 'b':
                if 'a' in results:
                    #print("reuse a")
                    # re.sub(r'a','b',results) # only on first occurrence
                    results=results.replace('a', 'b', 1)
                else:
                    print('ERROR: Out of sequence - ', logString, logChar, results, '-1')
                    OutOfSequence = True
                    break
            elif logChar == 'c':
                if 'b' in results:
                    #print('reuse b')
                    results = results.replace('b', 'c', 1)
                else:
                    print('ERROR: Out of sequence - ', logString, logChar, results, '-1')
                    OutOfSequence = True
                    break
            elif logChar == 'd':
                if 'c' in results:
                    #print('reuse c')
                    results = results.replace('c', 'd', 1)
                else:
                    print('ERROR: Out of sequence - ', logString, logChar, results, '-1')
                    OutOfSequence = True
                    break
            elif logChar == 'e':
                if 'd' in results:
                    #print('reuse d')
                    results = results.replace('d', 'e', 1)
                else:
                    print('ERROR: Out of sequence - ', logString, logChar, results, '-1')
                    OutOfSequence = True
                    break
        if not OutOfSequence:
            print(len(results), results)
        #results = []
        results=''
    example+=1

