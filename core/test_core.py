from main.menu import Body

from core.exceptions import ParametroNegativoException

import pytest

def test_vinte():
    """
    Teste com:
        notas: 1, 2, 5, 10
        valo: 20
    """
    x = Body.main([1, 2, 5, 10], 20)
    assert x[0] == 'Nota: 10, quantidade: 2'

def test_cinquenta_e_tres():
    """
    Teste com:
        notas: 1, 2, 5, 10
        valo: 53
    """
    x = Body.main([1, 2, 5, 10], 53)
    assert x[0] == 'Nota: 10, quantidade: 5'
    assert x[1] == 'Nota: 2, quantidade: 1'
    assert x[2] == 'Nota: 1, quantidade: 1'
    assert x[3] == 'resto: 0'

def test_cinquenta_e_quatro():
    """
    Teste com:
        notas: 10
        valo: 54
    """
    x = Body.main([10], 54)
    assert x[0] == 'Nota: 10, quantidade: 5'
    assert x[1] == 'resto: 4'

#def test_menos_um():
#    assert AssertionError(Body.main([-1], -1)) == ParametroNegativoException('Valor negativo!')
