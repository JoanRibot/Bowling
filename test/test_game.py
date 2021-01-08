from src.game import *

def test_simbolo_a_numero():
    assert Bowling.simbolo_a_numero("X")==("10")
    assert Bowling.simbolo_a_numero("/")==("10")
    assert Bowling.simbolo_a_numero("-")==("0")

def test_spike():
    assert Bowling.spike("1/111111111111111111",1)==10
    assert Bowling.spike("-/X--X--X--X--X--",1)==20
    assert Bowling.spike("25XXX4/2111XX43",6)==8
    assert Bowling.spike("XXX-/145136/9/154",13)==2

def test_strike():
    assert Bowling.strike("X111111111111111111",0)==12
    assert Bowling.strike("--X--X--X--X--X--",14)==10
    assert Bowling.strike("25XXX4/2111XX43",3)==24
    assert Bowling.strike("25XXX4/2111XX43",2)==30
    assert Bowling.strike("25XXX4/2111XX43",4)==20

def test_suma_puntos():
    assert Bowling("11111111111111111111").suma_puntos()==20
    assert Bowling("12345123451234512345").suma_puntos()==60
    assert Bowling("9-9-9-9-9-9-9-9-9-9-").suma_puntos()==90
    assert Bowling("5/5/5/5/5/5/5/5/5/5/5").suma_puntos()==150
    assert Bowling("XXXXXXXXXXXX").suma_puntos()==300
    assert Bowling("XXX9-9-9-9-9-9-9-").suma_puntos()==141
    assert Bowling("8-7-539/9/X8-513/9-").suma_puntos()==122
    assert Bowling("8/9-44729-XX8-359/7").suma_puntos()==133
    assert Bowling("-/-/-/-/-/-/-/-/-/-/-").suma_puntos()==100
    assert Bowling("X5/X5/XX5/--5/X5/").suma_puntos()==175
    assert Bowling("8/549-XX5/53639/9/X").suma_puntos()==149













