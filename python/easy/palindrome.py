def getDigitList(x: int) -> list:
    """ Convert a number into a list of it's digits in reversed order.
    """
    digits = []

    while x >= 10:
        digits.append(x % 10)
        x = int(x / 10)

    digits.append(x)

    return digits


def isPalindrome(x: int) -> bool:
    """ Check if a number is a palindrome.
    """
    # if negative it can't be a palindrome
    if x < 0:
        return False

    # get list of digits and a reversed version
    digits = getDigitList(x)

    # compare first and last digit and then remove them from the list
    while len(digits) > 0:
        if digits[0] != digits[-1]:
            return False
        del (digits[0])
        # if only one element was left then it's not possible to remove another element
        try:
            del (digits[-1])
        except IndexError:
            pass

    return True


print(isPalindrome(12321))
