from ..tradutor_mt.simbolos_nao_usados import (
    LIBRA, CENTAVO, PARAGRAFO
)


def test_libra():
    assert LIBRA == '£'


def test_centavo():
    assert CENTAVO == '¢'


def test_paragrafo():
    assert PARAGRAFO == '§'
