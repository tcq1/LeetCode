def isSubsequence(s: str, t: str) -> bool:
    # iterate over source string
    for current_letter in s:
        if current_letter in t:
            first_occurrence_index = t.index(current_letter)
            t = t[first_occurrence_index + 1:]
        else:
            return False

    return True


print(isSubsequence("abc", "ahbgdc"))

# 99.61%, 82.20%