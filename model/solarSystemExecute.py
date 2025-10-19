import json 
from model.planet import Planet
import os
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))

class SolarSystemExecuter:
    
    def __init__(self, data_file=os.path.realpath(os.path.join(dir_path,'..','data','data_solar_system.json'))):
        self.data_file = data_file
        self.planets = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.planets = [Planet.from_dict(planet_data) for planet_data in data]
                    num_planets=len(self.planets)
                print(f"found {num_planets} planets from {self.data_file}")
            except Exception as e:
                print(f"error in loading a data: {e}- {traceback.format_exc()}. existing data will be used")
                self.create_default_data()
        
    
    def create_default_data(self):
        self.planets = [
            Planet("Mercury", 3.301e23, 57900000, []),
            Planet("Venus", 4.867e24, 108200000, []),
            Planet("Earth", 5.972e24, 149600000, ["Moon"]),
            Planet("Mars", 6.417e23, 227900000, ["Phobos", "Deimos"]),
            Planet("Jupiter", 1.898e27, 778500000, ["Io", "Europa", "Ganymede", "Callisto"]),
            Planet("Saturn", 5.683e26, 1432000000, ["Titan", "Rhea", "Iapetus", "Dione"]),
            Planet("Uranus", 8.681e25, 2867000000, ["Titania", "Oberon", "Umbriel", "Ariel"]),
            Planet("Neptune", 1.024e26, 4515000000, ["Triton", "Proteus", "Nereid"]),
            Planet("Pluto", 1.309e22, 5906400000, ["Charon", "Styx", "Nix"])
        ]
    
    def save_data_json(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump([planet.to_dict() for planet in self.planets], f, indent=2)
            print(f"Saved {len(self.planets)} planets to {self.data_file}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def get_planet(self, planet_name):
        if not planet_name:
            return None
            
        planet_name_lower = planet_name.lower()
        for planet in self.planets:
            if planet.name.lower() == planet_name_lower:
                return planet
        return None
    
    def get_all_planet_names(self):
        return [planet.name for planet in self.planets]
    
    def get_planet_mass(self, planet_name):
        planet = self.get_planet(planet_name)
        return planet.mass_kg if planet else None
    
    def get_planet_distance(self, planet_name):
        planet = self.get_planet(planet_name)
        return planet.distance_from_sun_km if planet else None
    
    def get_planet_moons(self, planet_name):
        planet = self.get_planet(planet_name)
        return planet.moons if planet else None
    
    def get_moon_count(self, planet_name):
        planet = self.get_planet(planet_name)
        return len(planet.moons) if planet else None
    
    def is_planet_in_list(self, planet_name):
        return self.get_planet(planet_name) is not None
