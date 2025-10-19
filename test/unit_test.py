import unittest
import os
import sys

sys.path.append(os.path.realpath("."))
sys.path.append(os.path.realpath("./SolarSystemApp"))
from SolarSystemApp.model.planet import Planet
from SolarSystemApp.model.solarSystemExecute import SolarSystemExecuter
from SolarSystemApp.model.queryExecuter import QueryExecuter

class TestSolarSystemApp(unittest.TestCase):
    
    def setUp(self):
        self.data_test_file = os.path.join(os.path.realpath("./SolarSystemApp/data"), 'data_solar_system.json')
        
        # Create test planet data
        self.test_planets = [
            Planet("Earth", 5.972e24, 149600000, ["Moon"]),
            Planet("Mars", 6.417e23, 227900000, ["Phobos", "Deimos"]),
            Planet("Jupiter", 1.898e27, 778500000, ["Io", "Europa", "Ganymede", "Callisto"])
        ]
    
   
    
    
    def test_planet_from_dict(self):
        """Test Planet creation from dictionary"""
        planet_data = {
            'name': 'anyPlanet',
            'mass_kg': 10000,
            'distance_from_sun_km': 50000000000,
            'moons': ['Moonx', 'Moony']
        }
        
        planet = Planet.from_dict(planet_data)
        self.assertEqual(planet.name, 'anyPlanet')
        self.assertEqual(planet.mass_kg, 10000)
        self.assertEqual(planet.distance_from_sun_km, 50000000000)
        self.assertEqual(planet.moons, ['Moonx', 'Moony'])
    
    def test_solar_system_executer_creation(self):
        """Test SolarSystemExecuter creation"""
        executer = SolarSystemExecuter(self.data_test_file)
        self.assertEqual(len(executer.planets), 9)  # Default data has 9 planets
    
    def test_get_planet(self):
        """Test getting planet by name"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        # Test existing planet
        earth = executer.get_planet("Earth")
        self.assertIsNotNone(earth)
        self.assertEqual(earth.name, "Earth")
        
        # Test case insensitive
        earth_lower = executer.get_planet("earth")
        self.assertIsNotNone(earth_lower)
        self.assertEqual(earth_lower.name, "Earth")
        
        # Test non-existent planet
        unknown = executer.get_planet("UnknownPlanet")
        self.assertIsNone(unknown)
    
    def test_get_planet_mass(self):
        """Test getting planet mass"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        mass = executer.get_planet_mass("Earth")
        self.assertEqual(mass, 5.972e24)
        
        # Test non-existent planet
        mass_unknown = executer.get_planet_mass("UnknownPlanet")
        self.assertIsNone(mass_unknown)
    
    def test_get_planet_distance(self):
        """Test getting planet distance"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        distance = executer.get_planet_distance("Earth")
        self.assertEqual(distance, 149600000)
    
    def test_get_planet_moons(self):
        """Test getting planet moons"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        moons = executer.get_planet_moons("Mars")
        self.assertEqual(moons, ["Phobos", "Deimos"])
    
    def test_get_moon_count(self):
        """Test getting moon count"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        # Planet with moons
        moon_count_mars = executer.get_moon_count("Mars")
        self.assertEqual(moon_count_mars, 2)
        
        # Planet without moons
        moon_count_venus = executer.get_moon_count("Venus")
        self.assertEqual(moon_count_venus, 0)
    
    def test_is_planet_in_list(self):
        """Test checking if planet exists"""
        executer = SolarSystemExecuter(self.data_test_file)
        
        # Existing planet
        self.assertTrue(executer.is_planet_in_list("Earth"))
        
        # Non-existent planet
        self.assertFalse(executer.is_planet_in_list("UnknownPlanet"))
        
        # Case insensitive
        self.assertTrue(executer.is_planet_in_list("earth"))
    
    
    def test_get_all_planet_names(self):
        executer = SolarSystemExecuter(self.data_test_file)
        names = executer.get_all_planet_names()
        
        expected_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", 
                         "Saturn", "Uranus", "Neptune", "Pluto"]
        
        self.assertEqual(names, expected_names)
        


if __name__ == '__main__':
    unittest.main()