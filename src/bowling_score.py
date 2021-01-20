class Bowling_score:

    def __init__(self,bowling_card):
        self.bowling_card = bowling_card
        self.especial_throws = ["-","/","X"]
        self.pins = 10
        self.frames = 10

    def simbol_to_number(simbol, pins):
        if simbol == "X":
            return pins
        if simbol == "/":
            return pins
        if simbol == "-":
            return 0
    
    def spare(bowling_card,counter,pins,especial_throws):
        throw1 = (bowling_card[counter+1])
        previous_throw=(bowling_card[counter-1])
        if throw1 in especial_throws:
            throw1 = Bowling_score.simbol_to_number(throw1,pins)
        if previous_throw == "-":
            previous_throw = 0
        return pins + int(throw1) - int(previous_throw)

    def strike(bowling_card,counter,pins,especial_throws): 
        throw1 = (bowling_card[counter+1])
        throw2 = (bowling_card[counter+2])
        if throw1 in especial_throws:
            throw1 = Bowling_score.simbol_to_number(throw1,pins)
        if throw2 in especial_throws:
            if throw2 == "/":
                throw1 = 0
            throw2 = Bowling_score.simbol_to_number(throw2,pins)
        return pins + int(throw1) + int(throw2)
    
    def is_especial_last_frame(bowling_card, frames, counter):
        formula_extra_throws = (len(bowling_card) - bowling_card.count("X")) /2 + bowling_card.count("X")
        especial_spare = bowling_card[counter-1] == "/" and len(bowling_card) == counter+1
        especial_strike = bowling_card[counter-1] == "X" and len(bowling_card) == counter+2
        return formula_extra_throws > frames and especial_spare or especial_strike


    def sum_points(self):
        sum=0
        counter=-1
        for i in self.bowling_card:
            counter+=1
            if Bowling_score.is_especial_last_frame(self.bowling_card, self.frames, counter):
                return sum
            if i not in self.especial_throws:
                sum += int(i)
            elif i == "-":
                pass
            elif i == "/":
                sum += Bowling_score.spare(self.bowling_card, counter, self.pins, self.especial_throws)
            elif i == "X":
                sum += Bowling_score.strike(self.bowling_card, counter, self.pins, self.especial_throws)
        return sum




