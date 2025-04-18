from bank import value


def test_hello():
    assert value("hello") == 0


def test_mix_hello():
    assert value("HeLLo yo") == 0


def test_h():
    assert value("hey") == 20


def test_other_hello():
    assert value("privet") == 100


def test_hless():
    assert value("g'morning") == 100
