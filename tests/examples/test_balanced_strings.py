from examples.balanced_strings import (
    balanced_parens_checker,
    generalized_balanced_checker,
)


class TestStackExamplesBalancedParens(object):
    def test__empty_string__true(self):
        assert balanced_parens_checker("") == True

    def test__single_open_parens__false(self):
        assert balanced_parens_checker("(") == False

    def test__single_close_parens__false(self):
        assert balanced_parens_checker(")") == False

    def test__balanced_parens__true(self):
        assert balanced_parens_checker("()") == True
        assert balanced_parens_checker("((()))") == True
        assert balanced_parens_checker("((()))()()") == True
        assert balanced_parens_checker("(())((()))") == True

    def test__unbalanced_parens__false(self):
        assert balanced_parens_checker("(((()))") == False
        assert balanced_parens_checker("(()") == False
        assert balanced_parens_checker("((") == False


class TestStackExamplesiGeneralizedBalancedChecker(object):
    def test__empty_string__true(self):
        assert generalized_balanced_checker("") == True

    def test__single_open_symbol__false(self):
        assert generalized_balanced_checker("(") == False

    def test__multiple_open_symbols__false(self):
        assert generalized_balanced_checker("([{") == False

    def test__multiple_closing_symbols__false(self):
        assert generalized_balanced_checker(")]}") == False

    def test__balanced_symbols__true(self):
        assert generalized_balanced_checker("([{}])") == True
        assert generalized_balanced_checker("[]{{([][])}()}") == True

    def test__unbalanced_symbols__false(self):
        assert generalized_balanced_checker("([{}]") == False
