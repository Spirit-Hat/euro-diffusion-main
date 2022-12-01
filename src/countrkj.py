from typing import List
from .city import City


class Countrkj:
    def __init__(self, name: str):
        self.name = name
        #CI -cities
        self.CI: List[City] = []
        self.full = False
        self.DAYOFFFULL = -1

    def __eq__(self, other):
        return self.DAYOFFFULL == other.DAYOFFFULL

    def __lt__(self, other):
        return self.DAYOFFFULL < other.DAYOFFFULL

    #ap function that added the city
    def ap(self, city: City) -> None:
        self.CI.append(city)

    def check_fullness(self, day) -> None:
        if self.full:
            return
        for city in self.CI:
            if city.full is False:
                return
        self.full = True
        self.DAYOFFFULL = day

    def has_foreign_neighbours(self) -> bool:
        for city in self.CI:
            for neighbour in city.neighbours:
                if neighbour.country_name != self.name:
                    return True

    def only_country_mode(self) -> None:
        self.full = True
        self.DAYOFFFULL = 0
