import shared as sh
import pytest

sh.afunction()

def test_multi_spaces():
    assert sh.space_compress('word       word     word') == 'word word word', "Failed multi space"


def test_multi_lines():
    multiline = """
    word
    word
    word
    """
    assert sh.space_compress(multiline) == 'word word word', "Failed multi line"


def test_assert_int():
    with pytest.raises(Exception) as exc_mssg:
        sh.space_compress(2)

    assert "Expected str but got" in str(exc_mssg)
    assert "int" in str(exc_mssg)


def test_assert_bool():
    with pytest.raises(Exception) as exc_mssg:
        sh.space_compress(False)

    assert "Expected str but got" in str(exc_mssg)
    assert "bool" in str(exc_mssg)

def test_square():
    with pytest.raises(Exception) as exc_mssg:
        sh.square_func(word)

    assert "Expected int but got" in str(exc_mssg):
    assert "str" in str(exc_mssg)

test_multi_spaces()
test_multi_lines()
test_assert_int()
test_assert_bool() 
test_square()