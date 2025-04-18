from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("HELLO") == "HLL"


def test_mix():
    assert shorten("HeLlO") == "HLl"


def test_num():
    assert shorten("r00t") == "r00t"


def test_punct():
    assert shorten("hello!") == "hll!"


def test_empty():
    assert shorten("") == ""


def test_vow():
    assert shorten("ieaiaio") == ""
