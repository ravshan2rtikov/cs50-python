from numb3rs import validate


def test_vadress():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True


def test_invadress():
    assert validate("255.255.255") == False
    assert validate("255.255.255.255.255") == False
    assert validate("256.257.258.259") == False
    assert validate("127.256.0.1") == False


def test_mixadress():
    assert validate("not.val.ip.adr") == False
    assert validate("127.0.0.1.home") == False
    assert validate(" 127.0.0.1") == False
    assert validate("127.0.0.1 ") == False
    assert validate("127/0-0:1") == False
