# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass demonstrating inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!")

# Another subclass for encapsulation example
class StealthHero(Superhero):
    def __init__(self, name, power, origin, stealth_level):
        super().__init__(name, power, origin)
        self.__stealth_level = stealth_level  # private attribute

    def reveal_stealth(self):
        print(f"{self.name}'s stealth level is {self.__stealth_level}")

# Example usage
hero1 = Superhero("Light", "Light Manipulation", "Nebula-9")
hero2 = FlyingHero("Skyler", "Wind Control", "Aero City", 555)
hero3 = StealthHero("Shadowmask", "Invisibility", "Nightfall Zone", 55)

hero1.introduce()
hero2.use_power()
hero3.reveal_stealth()
