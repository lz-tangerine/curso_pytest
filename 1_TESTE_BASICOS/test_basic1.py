from funcoes import is_positive


def test_eh_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False
