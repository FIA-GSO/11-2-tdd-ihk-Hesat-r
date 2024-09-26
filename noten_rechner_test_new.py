import pytest
from noten_rechner import *
testdatanoten = [
    (100, 'sehr gut'),
    (92, 'sehr gut'),
    (91, 'gut'),
    (81, 'gut'),
    (80, 'befriedigend'),
    (67, 'befriedigend'),
    (66, 'ausreichend'),
    (50, 'ausreichend'),
    (49, 'mangelhaft'),
    (30, 'mangelhaft'),
    (29, 'ungenügend'),
    (0, 'ungenügend'),
    (-1, ValueError),
    (101, ValueError),
    ('text', TypeError)
]
@pytest.mark.parametrize("value,expected", testdatanoten)
def test_noten_ausrechnen__noten_werden_korrekt_berechnet(value,expected):
    if(expected == ValueError):
        with pytest.raises(ValueError):
            noten_ausrechnen(value)
    elif(expected == TypeError):
        with pytest.raises(TypeError):
            noten_ausrechnen(value)
    else:
        # Act
        ist_ergebnis = noten_ausrechnen(value)

        assert ist_ergebnis == expected

## Prozent ##
testdataprozent = [
    (99, 100, 99),
    (25, 50, 50),
    ('text', 100, TypeError),
    (100, 'text', TypeError),
    (99.5, 100, TypeError),
    (99, 100.5, TypeError),
    (-1, 100, ValueError),
    (101, 100, ValueError)
]
@pytest.mark.parametrize("erreicht,maximal,ergebnis", testdataprozent)
def test_prozent_berechen__prozente_werden_korrekt_berechnet(erreicht,maximal,ergebnis):
    if(ergebnis == ValueError):
        with pytest.raises(ValueError):
            prozent_berechnen(erreicht, maximal)
    elif(ergebnis == TypeError):
        with pytest.raises(TypeError):
            prozent_berechnen(erreicht, maximal)
    else:
        # Act
        ist_ergebnis = prozent_berechnen(erreicht, maximal)

        assert ist_ergebnis == ergebnis