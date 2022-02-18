import re
from film import *
from seat import *
from spectator import *
import random as rand


class Cinema:
    def __init__(self, rows:int, columns:int, film:Film) -> None:
            self.film = film
            self.seats = create_seats(rows, columns)
            self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            self.rows = rows
            self.columns = columns

    def allocate_spectators(self, spectatorList):
        
        def findSeat(self, row:int, column:str) -> Seat:
            for seat in self.seats:
                if seat.row == row and seat.letter == column:
                    return seat
            print(f'row : {row}, letter {column}')
            print('Seat not found !')

        min_age = self.film.min_age
        price = self.film.ticket_price

        row = rand.randint(0, self.rows)
        column = rand.randint(0, self.columns-1)

        for spectator in spectatorList:
            
            row = rand.randint(1, self.rows)
            column = rand.randint(0, self.columns-1)
            seat = findSeat(self, row, self.alphabet[column])

            if len(self.get_allocated_spectators()) == self.columns*self.rows:
                print(f"Cinema is full !, we cannot add at {row} : {column}" )
                return


            while seat.is_occupied == True:
                print(f"Taken seat ! {row} : {column}, looking for different one" )
                seat = findSeat(self, rand.randint(1, self.rows), self.alphabet[rand.randint(0, self.columns-1)])

            if (spectator.age >= min_age and 
                spectator.money >= price):
                seat.is_occupied = True
                seat.spectator = spectator

    def get_allocated_spectators(self):
        spectators_allocated = []
        for seat in self.seats:
            if (seat.is_occupied):
                spectators_allocated.append(seat.spectator)
        return spectators_allocated

    def showSeats(self):
        width = 12*self.columns
        print("#"*width)
        print("#", end="")
        first_spaces = int(width/2 - 5)
        print(" " * first_spaces, end = "")
        print("SCREEN", end="")
        second_spaces = width - (first_spaces + 6 + 2)
        print(" " * second_spaces, end = "")
        print("#")
        print("#"*width)

        for seat in self.seats:
            string_first = " [   " + str(seat.row) + ","
            second_part = "  " + seat.letter + "] "
            if (seat.is_occupied):
                string_first = " [*S  ,"
                
                if (seat.spectator.id > 9):
                    second_part = "*" + str(seat.spectator.id) + "] "
                else:
                    second_part = " *" + str(seat.spectator.id) + "] "
                
            if (seat.letter == self.alphabet[self.columns-1]):
                print(string_first + second_part)
            else:
                print(string_first + second_part, end="")

    def getSeats(self):
        return self.seats

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def create_seats(rows, columns) -> list[Seat]:
        seats = []
        for i in range (1, rows+1):
            for j in range(columns):
                seats.append(Seat(i, alphabet[j]))
        return seats
