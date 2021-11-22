import re


def longestCommonPrefix(strings) -> str:
    """ Find the longest common prefix of a list of strings.
    """
    currentPrefix = ""
    nextPrefix = ""

    # try out prefixes of first word
    for letter in strings[0]:
        runSuccessful = True
        nextPrefix += letter

        # check if prefixes match prefixes of other words
        for string in strings:
            if not re.match("^" + nextPrefix, string):
                runSuccessful = False
                break

        if runSuccessful:
            currentPrefix = nextPrefix
        else:
            break

    return currentPrefix


words = ['apfle', 'apfcalypse', 'apfel', 'osaft']
print(longestCommonPrefix(words))
