import math

class Planet:
    G = 6.67E-11 # gravitational constant

    def __init__(self, px, py, vx=0.0, vy=0.0, m=0.0):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.m = m

    def radius(self, planet):
        return math.sqrt((self.px - planet.px)**2 + (self.py - planet.py)**2)

    def force(self, planet, r=0.0):
        return self.G * self.m * planet.m / r**2

    def __str__(self):
        return f"px: {self.px} py: {self.py} vx: {self.vx} vy: {self.vy} m: {self.m}"
    