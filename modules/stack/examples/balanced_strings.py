import typing

from modules.stack import Stack


def balanced_parens_checker(tokens: str) -> bool:
    """
    Write an algorithm that will read a string of parentheses from left to
    right and decide whether the symbols are balanced
    """
    idx: int = 0
    s = Stack()
    balanced: bool = True

    while idx < len(tokens):
        symbol = tokens[idx]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        idx += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def generalized_balanced_checker(
    tokens: str, supported_symbols: dict = {"opens": "({[", "closes": ")}]"}
) -> bool:
    """
    Write an algorithm that will read a string of supported_symbols from left to
    right and decide whether the symbols are balanced
    """
    idx: int = 0
    s = Stack()
    balanced: bool = True

    def is_closing(top_symbol, closing_symbol):
        return supported_symbols["opens"].index(top_symbol) == supported_symbols[
            "closes"
        ].index(closing_symbol)

    while idx < len(tokens):
        symbol = tokens[idx]
        if symbol in supported_symbols["opens"]:
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top_symbol = s.pop()
                if not is_closing(top_symbol, symbol):
                    balanced = False
        idx += 1

    if balanced and s.is_empty():
        return True
    else:
        return False
