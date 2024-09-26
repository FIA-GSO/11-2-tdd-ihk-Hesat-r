def prozent_berechnen(erreichte_punktzahl, maximal_punktzahl):
    if(not isinstance(erreichte_punktzahl, int)):
        raise TypeError
    if(not isinstance(maximal_punktzahl, int)):
        raise TypeError
    if(erreichte_punktzahl > maximal_punktzahl):
        raise ValueError
    if(erreichte_punktzahl < 0):
        raise ValueError
    return int((erreichte_punktzahl / maximal_punktzahl) * 100)

def noten_ausrechnen(prozentwert):
    if(not isinstance(prozentwert, int)):
        raise TypeError
    if(prozentwert < 0):
        raise ValueError
    if(prozentwert > 100): 
        raise ValueError
    if (prozentwert <= 100 and prozentwert >= 92):
        return"sehr gut"
    elif(prozentwert <= 91 and prozentwert >= 81):
        return "gut"
    elif(prozentwert <= 80 and prozentwert >= 67):
        return "befriedigend"
    elif(prozentwert <= 66 and prozentwert >= 50):
        return "ausreichend"
    elif(prozentwert <= 49 and prozentwert >= 30):
        return "mangelhaft"
    elif(prozentwert <= 29 and prozentwert >= 0):
        return "ungenügend"
    