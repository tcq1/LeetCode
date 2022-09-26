def isIsomorphic(s: str, t: str) -> bool:
    hash_table = {}

    # create a hash map
    for i in range(len(s)):
        # check if key already exists
        if s[i] not in hash_table.keys():
            # check if value already exists
            if t[i] not in hash_table.values():
                hash_table[s[i]] = t[i]
            else:
                return False
        else:
            if hash_table[s[i]] != t[i]:
                return False
    return True


print(isIsomorphic("badc", "baba"))
