class Seat:
    def __init__(self, row:int, letter:chr) -> None:
        self.row = row
        self.letter = letter
        self.is_occupied = False
        self.spectator = None

    def __str__(self):
        return f'row {self.row}, column {self.letter}, isOccupied {self.is_occupied}, spectator {self.spectator}'
    
    def __repr__(self):
        return str(self)