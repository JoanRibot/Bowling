from src.bowling_score import *

def test_simbolo_a_numero():
    assert Bowling_score.simbol_to_number("X",10)==(10)
    assert Bowling_score.simbol_to_number("/",10)==(10)
    assert Bowling_score.simbol_to_number("-",10)==(0)

def test_spare():
    assert Bowling_score.spare("1/111111111111111111",1,10,["-","/","X"])==10
    assert Bowling_score.spare("-/X--X--X--X--X--",1,10,["-","/","X"])==20
    assert Bowling_score.spare("25XXX4/2111XX43",6,10,["-","/","X"])==8
    assert Bowling_score.spare("XXX-/145136/9/154",13,10,["-","/","X"])==2

def test_strike():
    assert Bowling_score.strike("X111111111111111111",0,10,["-","/","X"])==12
    assert Bowling_score.strike("--X--X--X--X--X--",14,10,["-","/","X"])==10
    assert Bowling_score.strike("25XXX4/2111XX43",3,10,["-","/","X"])==24
    assert Bowling_score.strike("25XXX4/2111XX43",2,10,["-","/","X"])==30
    assert Bowling_score.strike("25XXX4/2111XX43",4,10,["-","/","X"])==20

def test_is_especial_last_frame():
    assert Bowling_score.is_especial_last_frame("X111111111111111111", 10, 0) == False
    assert Bowling_score.is_especial_last_frame("5/5/5/5/5/5/5/5/5/5/5", 10, 20) == True
    assert Bowling_score.is_especial_last_frame("8/549-XX5/53639/9/X", 10, 18) == True
    assert Bowling_score.is_especial_last_frame("9-9-9-9-9-9-9-9-9-9-", 10, 20) == False
    assert Bowling_score.is_especial_last_frame("XXXXXXXXXXXX", 10, 10) == True
   

def test_sum_points():
    assert Bowling_score("11111111111111111111").sum_points()==20
    assert Bowling_score("12345123451234512345").sum_points()==60
    assert Bowling_score("9-9-9-9-9-9-9-9-9-9-").sum_points()==90
    assert Bowling_score("5/5/5/5/5/5/5/5/5/5/5").sum_points()==150
    assert Bowling_score("XXXXXXXXXXXX").sum_points()==300
    assert Bowling_score("XXX9-9-9-9-9-9-9-").sum_points()==141
    assert Bowling_score("8-7-539/9/X8-513/9-").sum_points()==122
    assert Bowling_score("8/9-44729-XX8-359/7").sum_points()==133
    assert Bowling_score("-/-/-/-/-/-/-/-/-/-/-").sum_points()==100
    assert Bowling_score("X5/X5/XX5/--5/X5/").sum_points()==175
    assert Bowling_score("8/549-XX5/53639/9/X").sum_points()==149







