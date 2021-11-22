def lengthOfLongestSubstring(s: str) -> int:
    usedChars = {}

    longest = 0

    while len(s) != 0:
        for i in range(len(s)):
            if s[i] in usedChars.keys():
                if i > longest:
                    longest = i
                usedChars = {}
                s = s[i:]
                break
            else:
                usedChars[s[i]] = True

        if len(s) > longest:
            longest = len(s)

    return longest


print(lengthOfLongestSubstring("a"))
