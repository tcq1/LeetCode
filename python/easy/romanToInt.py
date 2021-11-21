def romanToInt(s: str) -> int:
    """ Convert a roman number (as a string) to an integer.
    """
    symbol_list = list(s)
    symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    result = 0

    while len(symbol_list) > 1:
        if symbol_dict[symbol_list[0]] >= symbol_dict[symbol_list[1]]:
            result += symbol_dict[symbol_list[0]]
            del symbol_list[0]
        else:
            result += symbol_dict[symbol_list[0] + symbol_list[1]]
            del symbol_list[0]
            del symbol_list[0]

    if len(symbol_list) == 1:
        result += symbol_dict[symbol_list[0]]

    return result


print(romanToInt('IX'))
