from funcoes import adding, lens


def test_sum_and_lens():
    assert adding(3, 2) == 5
    assert lens([1, 2, 3, 4, 5]) == 5
