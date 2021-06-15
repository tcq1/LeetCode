class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNumber(list_node: ListNode) -> int:
    """ Convert a ListNode into a number.

    :param list_node: ListNode
    :return: int
    """
    digits = []
    currentNode = list_node

    digits.append(currentNode.val)

    while currentNode.next is not None:
        currentNode = currentNode.next
        digits.append(currentNode.val)

    value = 0

    for exponent in range(len(digits)):
        value += digits[exponent] * 10 ** exponent

    return value


def getListNode(number: int) -> ListNode:
    """ Convert a number into a ListNode.
    Assuming that input is correct.

    :param number: int
    :return: ListNode
    """
    digits = []
    stringRep = str(number)

    for i in range(len(stringRep)):
        digits.append(int(stringRep[i]))

    linkedList = ListNode(digits.pop())
    lastNode = linkedList

    while len(digits) > 0:
        newNode = ListNode(digits.pop())
        lastNode.next = newNode
        lastNode = newNode

    return linkedList


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """ Add up the integer values of two ListNodes and return the sum as a ListNode.

    :param l1: first ListNode
    :param l2: second ListNode
    :return: ListNode
    """
    return getListNode(getNumber(l1) + getNumber(l2))


def toString(list_node: ListNode) -> str:
    """ Return a String representation of a ListNode.

    :param list_node: ListNode
    :return: string
    """
    currentNode = list_node

    output = str(currentNode.val)
    while currentNode.next is not None:
        currentNode = currentNode.next
        output += f"-{currentNode.val}"

    return output


l1 = getListNode(243)
l2 = getListNode(564)

outputListNode = addTwoNumbers(l1, l2)

print(toString(l1))
print(toString(l2))
print(toString(outputListNode))
