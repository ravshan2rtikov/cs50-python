from fuel import convert, gauge


def test_conv():
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/4") == 0


def test_conv_err():
    try:
        convert("3/four")
        assert False
    except ValueError:
        assert True

    try:
        convert("5/4")
        assert False
    except ValueError:
        assert True

    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        assert True


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
