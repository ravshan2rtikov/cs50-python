from plates import is_valid


def test_validation():
    assert is_valid("CS50") == True


def test_short():
    assert is_valid("C") == False


def test_long():
    assert is_valid("CS50CS50") == False


def test_begins_letter():
    assert is_valid("1CS50") == False
    assert is_valid("C150") == False


def test_start_2letters():
    assert is_valid("5CS0") == False


def test_start_two_letters():
    assert is_valid("C5CS50") == False


def test_zero_num():
    assert is_valid("CS05") == False


def test_mid_num():
    assert is_valid("CS5P0") == False


def test_symb():
    assert is_valid("CS.50") == False


def test_onlet():
    assert is_valid("HELLOW") == True


def test_end_num():
    assert is_valid("CS120") == True
