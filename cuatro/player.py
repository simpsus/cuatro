
class Player:
    """ Base class of a cuatro player """

    def __init__(self, name):
        self.name = name
        self.pieces = 15
        # the color is assigned by the Game, when the player is added.
        self.color = None

    def play(self, *args):
        print "not implemented"
        return []

    def place(self, *args):
        print "not implemented"


class Human(Player):
    """ A console-based human player. """

    def __init__(self, name):
        Player.__init__(self, name)

    def play(self, dice, board):
        print board
        print dice.throws, "\t", dice
        #da = DiceAnalyzer(dice)
        #da.probability_yahtzee()
        keep = raw_input("which numbers do you want to keep? ")
        return [int(k) for k in keep if k.isdigit()]

    def place(self, dice, board):
        print board
        print dice
        place = ""
        while len(place) != 2:
            place = raw_input("where to place your piece? ").upper()
        return place
