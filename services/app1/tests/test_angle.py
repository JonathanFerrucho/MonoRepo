import angle


def test_twelve():
    assert angle.between(12, 00) == 0
    assert angle.between(1, 00) == 30
    assert angle.between(1, 1) == 24.5
