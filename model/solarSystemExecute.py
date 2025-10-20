import json 
from model.planet import Planet
import os
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))

class SolarSystemExecuter:
    
    def __init__(self, data_file=os.path.realpath(os.path.join(dir_path,'..','data','data_solar_system.json'))):
        self.data_file = data_file
        self.planets = []
        self.load_data_planets()
    
    def load_data_planets(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.planets = []
                    for planet_data in data:
                        self.planets.append(Planet.from_dict(planet_data))
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
            Planet("Mars", 6.417e23, 227900000, ["Deimos","Phobos"]),
            Planet("Jupiter", 1.898e27, 778500000, ["Europa", "Io", "Ganymede", "Callisto"]),
            Planet("Saturn", 5.683e26, 1432000000, ["Titan", "Iapetus", "Rhea", "Dione"]),
            Planet("Uranus", 8.681e25, 2867000000, ["Titania", "Umbriel", "Oberon", "Ariel"]),
            Planet("Neptune", 1.024e26, 4515000000, ["Proteus","Triton", "Nereid"]),
            Planet("Pluto", 1.309e22, 5906400000, ["Styx","Charon", "Nix"])
        ]
    
    def get_planet(self, planet_name):
        if not planet_name:
            return None
            
        check_planet_name_lower = planet_name.lower()
        for planet_i in self.planets:
            if planet_i.name.lower() == check_planet_name_lower:
                return planet_i
        return None
    
    def get_all_planet_names(self):
        planet_all=[]
        for planet_i in self.planets:
            planet_all.append(planet_i.name)
        return planet_all
        
    def get_planet_mass(self, planet_name):
        planet = self.get_planet(planet_name)
        if planet:
            return planet.mass_kg
        else:
            return None
    
    def get_planet_distance(self, planet_name):
        planet = self.get_planet(planet_name)
        if planet:
            return planet.distance_from_sun_km 
        else:
            return None
    
    def get_planet_moons(self, planet_name):
        planet = self.get_planet(planet_name)
        if planet:
            return planet.moons 
        else:
            return None
    
    def get_moon_count(self, planet_name):
        planet = self.get_planet(planet_name)
        if planet:
            return len(planet.moons) 
        else:
            return None
    
    def is_planet_in_list(self, planet_name):
        return self.get_planet(planet_name) is not None
