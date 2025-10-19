import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Planet:
    
    def __init__(self, name, moons, mass_kg, distance_from_sun_km):
        self.name = name
        self.moons = moons
        self.mass_kg = mass_kg
        self.distance_from_sun_km = distance_from_sun_km
    
    def __str__(self):
        return f"{self.name}: {self.mass_kg:.2e} kg, {self.distance_from_sun_km:,.0f} km from Sun"
    
    def to_dict(self):
        return {
            'name': self.name,
            'mass_kg': self.mass_kg,
            'distance_from_sun_km': self.distance_from_sun_km,
            'moons': self.moons
        }
    
    @classmethod
    def from_dict(cls, input):
        return cls(
            input['name'],
            input['moons'],
            input['mass_kg'],
            input['distance_from_sun_km']
        )