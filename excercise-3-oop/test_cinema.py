from cinema import *
from film import *
from spectator import *
from seat import *

def shouldBeOneOccupiedSeat():
    
    cinema = Cinema(5, 5, Film('title', 120, 12, 'spielberg', 12.20))
    cinema.allocate_spectators([Spectator(1, 12, 13), Spectator(2, 11, 14)])
    
    assert cinema.get_allocated_spectators()[0] == (Spectator(1, 12, 13))
    print(f"{shouldBeOneOccupiedSeat.__name__} - passed !")

shouldBeOneOccupiedSeat()


cinema = Cinema(9, 9, Film('title', 120, 12, 'spielberg', 12.20))
cinema.showSeats()
cinema.allocate_spectators([
    Spectator(1, 12, 13), 
    Spectator(2, 13, 14),
    Spectator(3, 13, 14),
    Spectator(14, 13, 14),
    Spectator(4, 10, 15), # should not be assigned age
    Spectator(23, 10, 12.19), # should not be assigned price
    Spectator(5, 15, 15),
    Spectator(6, 15, 15),
    Spectator(7, 15, 15),
    Spectator(8, 15, 15)
    ])
cinema.showSeats()