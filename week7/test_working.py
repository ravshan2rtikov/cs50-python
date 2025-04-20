import pytest
from working import convert


def test_conv():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_night():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalids():
    with pytest.raises(ValueError):
        convert("9:69 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 AM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
