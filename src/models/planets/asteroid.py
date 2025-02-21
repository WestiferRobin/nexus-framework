from src.models.planets.planet import Planet
from src.utils.enums.planet_enums import PlanetType


class Asteroid(Planet):
    def __init__(self, name: str):
        super().__init__(name, PlanetType.Asteroid)

class AsteroidBelt:
    def __init__(self, name, m=1, n=1):
        self.name = name
        self.asteroids = {}
        for i in range(0, m):
            self.asteroids[i] = {}
            for j in range(0, n):
                index = i + j
                self.asteroids[i][j] = Asteroid(f"{name}'s Asteroid #{index}")