class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.wins = 0
        self.delta = 0
    
    def update(self, isWinner, score1, score2):
        if isWinner:
            self.wins += 1
            self.delta += score1 - score2
        else: 
            self.delta += score2 - score1
    