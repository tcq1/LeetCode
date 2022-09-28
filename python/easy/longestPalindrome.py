class Solution:
    def longestPalindrome(self, s: str) -> int:
        """ Find the length of the longest palindrome that can be created from a string.
        Use a set to remember letters that have already been seen, and remove letters if seen again.
        That way the length of half of the palindrome string can be calculated

        :param s: input string
        :return: length of the longest possible palindrome
        """
        # count palindrome length
        palindrome_length = 0

        # store seen letters in set, if seen again remove from set
        seen_letters = set()

        # loop through string
        for letter in s:
            if letter not in seen_letters:
                seen_letters.add(letter)
            else:
                seen_letters.remove(letter)
                palindrome_length += 1

        # double to get total palindrome length
        palindrome_length *= 2

        # if there are still letters in seen letters then there is at least one letter with uneven number of occurrences
        if len(seen_letters) > 0:
            palindrome_length += 1

        return palindrome_length


input_string = "abccccdd"
solution = Solution()
print(solution.longestPalindrome(input_string))
