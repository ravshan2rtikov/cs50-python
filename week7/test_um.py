from um import count


def test_um():
    assert count("um") == 1
    assert count("Um?") == 1
    assert count("Hey, um.. Are we going tonight?") == 1


def test_ums():
    assert count("um, ahh um..") == 2
    assert count("um, thanks, um..") == 2
    assert count("um um um um") == 4
    assert count("Um! um.. UM?") == 3


def test_insidum():
    assert count("yummy") == 0
    assert count("plenum and mumble rap") == 0
    assert count("aluminum is metal") == 0
