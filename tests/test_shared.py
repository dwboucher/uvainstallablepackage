import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_space_compress():
    test_str = "Word            Word         Word"

    assert "Word Word Word" == sh.space_compress(test_str), "Sting <{}> not compressed as expected".format(test_str)

@pytest.mark.xfail(reason ="Intentional Failure for Practice")
def test_xfail_space_compress():
    test_str = "Word Word Word   Word"
    assert "Word Word Word" == sh.space_compress(test_str), "Sting <{}> not compressed as expected".format(test_str)

@pytest.mark.skip(reason = "Intentional Skip for Practice")
def test_skip_space_compress():
    test_str = "Word Word Word Word"
    assert "Word Word Word" == sh.space_compress(test_str), "Sting <{}> not compressed as expected".format(test_str)

@pytest.mark.skipif(sys.platform == 'darwin', reason ="Skipped because of sys.platform = darwin")
def test_skipif_func():
    test_str = "This will not fail."
    print("My platform is: ", sys.platform)
    assert "This will not fail." == test_str, "These strings don't match"