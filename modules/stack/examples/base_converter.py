from modules.stack import Stack


def divide_by_2(num: int) -> str:
    """
    Takes an interger and returns its equivalent in binary
    """

    s = Stack()
    binary_str: str = ""

    if num == 0:
        s.push(num)

    while num > 0:
        num, remainder = divmod(num, 2)
        s.push(remainder)

    while not s.is_empty():
        digit = s.pop()
        binary_str += str(digit)

    return binary_str


def base_converter(num: int, base: int) -> str:
    """
    Ref: http://calc.50x.eu/
    """
    stack = Stack()
    converted_str: str = ""
    digits = "0123456789ABCDEF"

    if num == 0:
        stack.push(num)

    while num > 0:
        num, remainder = divmod(num, base)
        stack.push(remainder)

    while not stack.is_empty():
        digit = stack.pop()
        converted_str += digits[digit]

    return converted_str
