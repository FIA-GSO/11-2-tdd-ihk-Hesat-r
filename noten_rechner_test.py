import pytest
from noten_rechner import *

def test_noten_ausrechnen__höchste_sehr_gut_ausgabe():
    # Arrange
    prozentwert = 100
    soll_ergebnis = "sehr gut"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis
def test_noten_ausrechnen__niedrigste_sehr_gut_ausgabe():
    # Arrange
    prozentwert = 92
    soll_ergebnis = "sehr gut"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__höchste_gut_ausgabe():
    # Arrange
    prozentwert = 91
    soll_ergebnis = "gut"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis
def test_noten_ausrechnen__niedrigste_gut_ausgabe():
    # Arrange
    prozentwert = 81
    soll_ergebnis = "gut"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__höchste_befriedigend_ausgabe():
    # Arrange
    prozentwert = 80
    soll_ergebnis = "befriedigend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__niedrigste_befriedigend_ausgabe():
    # Arrange
    prozentwert = 67
    soll_ergebnis = "befriedigend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__höchste_ausreichend_ausgabe():
    # Arrange
    prozentwert = 66
    soll_ergebnis = "ausreichend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__niedrigste_ausreichend_ausgabe():
    # Arrange
    prozentwert = 50
    soll_ergebnis = "ausreichend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis


def test_noten_ausrechnen__höchste_mangelhaft_ausgabe():
    # Arrange
    prozentwert = 49
    soll_ergebnis = "mangelhaft"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__niedrigste_mangelhaft_ausgabe():
    # Arrange
    prozentwert = 30
    soll_ergebnis = "mangelhaft"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__höchste_ungenügend_ausgabe():
    # Arrange
    prozentwert = 29
    soll_ergebnis = "ungenügend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis
def test_noten_ausrechnen__niedrigste_ungenügend_ausgabe():
    # Arrange
    prozentwert = 0
    soll_ergebnis = "ungenügend"

    # Act
    ist_ergebnis = noten_ausrechnen(prozentwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_noten_ausrechnen__grenzwert_unterschritten():
    # Arrange
    prozentwert = -1

    # Act
    with pytest.raises(ValueError):
        noten_ausrechnen(prozentwert)

def test_noten_ausrechnen__grenzwert_überschritten():
    # Arrange
    prozentwert = 101

    # Act
    with pytest.raises(ValueError):
        noten_ausrechnen(prozentwert)

def test_noten_ausrechnen__falsche_argumente():
    # Arrange
    prozentwert = "t"

    # Act
    with pytest.raises(TypeError):
        noten_ausrechnen(prozentwert)


# Test prozent berechnen #
def test_prozent_berechnen__richtige_prozent_ausgabe():
    # Arrange
    erreichte_punktzahl = 98
    maximal_punktzahl = 100
    soll_ergebnis = 98

    # Act
    ist_ergebnis = prozent_berechnen(erreichte_punktzahl, maximal_punktzahl)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_prozent_berechnen__grenzwert_unterschritten():
    # Arrange 
    erreichte_punktzahl = -1
    maximal_punktzahl = 100

    # Act
    with pytest.raises(ValueError):
        prozent_berechnen(erreichte_punktzahl, maximal_punktzahl)

def test_prozent_berechnen__grenzwert_überschritten():
    # Arrange 
    erreichte_punktzahl = 101
    maximal_punktzahl = 100

    # Act
    with pytest.raises(ValueError):
        prozent_berechnen(erreichte_punktzahl, maximal_punktzahl)

def test_prozent_berechnen__falsche_argumente():
    # Arrange 
    erreichte_punktzahl = "t"
    maximal_punktzahl = 100

    # Act
    with pytest.raises(TypeError):
        prozent_berechnen(erreichte_punktzahl, maximal_punktzahl)

def test_prozent_berechnen__falsche_argumente2():
    # Arrange 
    erreichte_punktzahl = 100
    maximal_punktzahl = "t"

    # Act
    with pytest.raises(TypeError):
        prozent_berechnen(erreichte_punktzahl, maximal_punktzahl)
