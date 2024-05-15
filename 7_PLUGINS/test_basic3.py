from funcoes import email_valido, dividir, adding, lens, is_positive


def test_email_valido():
    assert email_valido('exemplo@dominio.com') is True
    assert email_valido('exemplo.com') is False


def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(4, 0) is None

def test_sum_and_lens():
    assert adding(3, 2) == 5
    assert lens([1, 2, 3, 4, 5]) == 5

def test_eh_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False