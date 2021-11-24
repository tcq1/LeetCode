def isValid(string):
    """ Check whether a string has valid parentheses (closed parentheses and closing order).
    """
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    # use a stack to remember order
    stack = []

    try:
        # check every symbol of string
        for symbol in string:
            if symbol in bracket_pairs.keys():
                # add to stack if opening bracket
                stack.append(bracket_pairs[symbol])
            elif symbol in bracket_pairs.values():
                # remove from stack if closing bracket
                if stack[-1] != symbol:
                    # fail if wrong order
                    return False
                else:
                    stack.pop()
    except IndexError:
        # fail if tried to remove from empty stack
        return False

    # check that stack is empty at the end
    return len(stack) == 0


print(isValid('{()}'))
