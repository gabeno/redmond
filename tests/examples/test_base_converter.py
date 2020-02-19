from examples.base_converter import divide_by_2, base_converter

class TestDivideBy2(object):
    def test__int_0__returns_0(self):
        assert divide_by_2(0) == "0"

    def test__int_1__returns_1(self):
        assert divide_by_2(1) == "1"

    def test__int_2__returns_10(self):
        assert divide_by_2(2) == "10"

    def test__int_3__returns_11(self):
        assert divide_by_2(3) == "11"

    def test__int_20__returns_10100(self):
        assert divide_by_2(20) == "10100"


class TestBaseConverter(object):
    # base 2
    def test__base_2_with_int_0__returns_0(self):
        assert base_converter(0, 2) == "0"

    def test__base_2_with_int_1__returns_1(self):
        assert base_converter(1, 2) == "1"

    def test__base_2_with_int_2__returns_10(self):
        assert base_converter(2, 2) == "10"

    def test__base_2_with_int_3__returns_11(self):
        assert base_converter(3, 2) == "11"

    def test__base_2_with_int_20__returns_10100(self):
        assert base_converter(20, 2) == "10100"

    # base 16
    def test__base_16_with_int_0__returns_0(self):
        assert base_converter(0, 16) == "0"

    def test__base_16_with_int_1__returns_1(self):
        assert base_converter(1, 16) == "1"

    def test__base_16_with_int_9__returns_9(self):
        assert base_converter(9, 16) == "9"

    def test__base_16_with_int_10__returns_A(self):
        assert base_converter(10, 16) == "A"

    def test__base_16_with_int_15__returns_F(self):
        assert base_converter(15, 16) == "F"

    def test__base_16_with_int_17__returns_11(self):
        assert base_converter(17, 16) == "11"

    def test__base_16_with_int_20__returns_14(self):
        assert base_converter(20, 16) == "14"

    def test__base_16_with_int_63__returns_3F(self):
        assert base_converter(63, 16) == "3F"

    # base 8
    def test__base_8_with_int_0__returns_0(self):
        assert base_converter(0, 8) == "0"

    def test__base_8_with_int_1__returns_1(self):
        assert base_converter(1, 8) == "1"

    def test__base_8_with_int_9__returns_11(self):
        assert base_converter(9, 8) == "11"

    def test__base_8_with_int_10__returns_12(self):
        assert base_converter(10, 8) == "12"

    def test__base_8_with_int_15__returns_17(self):
        assert base_converter(15, 8) == "17"

    def test__base_8_with_int_17__returns_21(self):
        assert base_converter(17, 8) == "21"

    def test__base_8_with_int_20__returns_24(self):
        assert base_converter(20, 8) == "24"

    def test__base_8_with_int_63__returns_77(self):
        assert base_converter(63, 8) == "77"
