import re
class QueryExecuter:
    """Class to cehck extended questions on the queries about planets"""
    
    def __init__(self, solar_system_manager):
        self.manager = solar_system_manager
        
        # define possible quires to capture different types of quires  
        self.qureyadd = {
            'everything': [
                r'tell me everything about (\w+)',
                r'show me all information about (\w+)',
                r'what can you tell me about (\w+)',
            ],
            'mass': [
                r'how massive is (\w+)',
                r"what's the mass of (\w+)",
                r'how much does (\w+) weigh'
            ],
            'distance': [
                r'how far is (\w+) from the sun',
                r"what is (\w+)'s distance from the sun",
                r'distance of (\w+) from sun',
            ],
            'moons': [
                r'what moons does (\w+) have',
                r'list the moons of (\w+)',
                r'what are the moons orbiting (\w+)'
            ],
            'moon_count': [
                r'how many moons does (\w+) have',
                r"how many moons has (\w+)",
                r"what is the number of moons of (\w+)",
            ],
            'is_exist': [
                r'is (\w+) in the list of planets',
                r'is (\w+) included in the list',
            ],
            'list_planets': [
                r'list all planets',
                r'show me all planets',
                r'name all the planets'
            ]
        }
    
    def search_planet_name(self, query, diff_query):
        
        for query_i in diff_query:
            match = re.search(query_i, query.lower())
            if match:
                return match.group(1).title()  
        return None
    
    def process_query(self, query):
        query_lower = query.lower().strip()
        
        # Check for each query type
        for query_type, diff_query in self.qureyadd.items():
            planet_name = self.search_planet_name(query_lower, diff_query)
            
            if planet_name:
                return self.execute_query(query_type, planet_name)
        
        # if thre is no query matching to the question then return the help message
        return self.reply_unclear_questions()
    
    def execute_query(self, query_type, planet_name):
        if query_type == 'moon_count':
            return self.get_moon_count_response(planet_name)
        elif query_type == 'is_exist':
            return self.check_existence_response(planet_name)
            
        elif query_type == 'everything':
            return self.check_everything_response(planet_name)
        
        elif query_type == 'mass':
            return self.get_mass_response(planet_name)
        elif query_type == 'distance':
            return self.get_distance_response(planet_name)
        
        elif query_type == 'moons':
            return self.check_moons_response(planet_name)

        elif query_type == 'list_planets':
            return self.get_list_planets_response()
        else:
            return "i can not find the quesion on the query."
    
    def check_everything_response(self, planet_name):
        check_planet = self.manager.get_planet(planet_name)
        if not check_planet:
            return f"NO information about '{planet_name}' in query."
        
        response = f"you can find detail infromation below  about {check_planet.name}:\n\n"
        response += f"Name: {check_planet.name}\n"
        response += f"Mass: {check_planet.mass_kg:.2e} kg\n"
        response += f"Distance from Sun: {check_planet.distance_from_sun_km:,.0f} km\n"
        response += f"Number of moons: {len(check_planet.moons)}\n"
        
        if check_planet.moons:
            response += f"Moons: {', '.join(check_planet.moons)}\n"
        else:
            response += "Moons: None\n"
        
        return response
    
    def get_mass_response(self, planet_name):
        mass = self.manager.get_planet_mass(planet_name)
        if mass is None:
            return f"NO mass information for '{planet_name}'."
        
        return f"The mass of {planet_name} is {mass:.2e} kg."
    
    def get_distance_response(self, planet_name):
        distance = self.manager.get_planet_distance(planet_name)
        if distance is None:
            return f"NO distance information for '{planet_name}'."
        
        return f"{planet_name} is {distance:,.0f} km from the Sun."
    
    def check_moons_response(self, planet_name):
        moons = self.manager.get_planet_moons(planet_name)
        if moons is None:
            return f"NO moon information for '{planet_name}'."
        
        if moons:
            moon_list = ', '.join(moons)
            return f"The moons of {planet_name} are: {moon_list}"
        else:
            return f"{planet_name} has no moons."
    
    def get_moon_count_response(self, planet_name):
        moon_count = self.manager.get_moon_count(planet_name)
        if moon_count is None:
            return f"NO moon information for '{planet_name}'."
        
        if moon_count == 1:
            return f"{planet_name} has {moon_count} moon."
        else:
            return f"{planet_name} has {moon_count} moons."
    
    def check_existence_response(self, planet_name):
        exists = self.manager.is_planet_in_list(planet_name)
        if exists:
            return f"Yes, {planet_name} is in my list of planets."
        else:
            return f"No, {planet_name} is not in my list of planets."
    
    def get_list_planets_response(self):
        planets = self.manager.get_all_planet_names()
        return f"The planets in my database are: {', '.join(planets)}"
    
    def reply_unclear_questions(self):
        help_text = """ the questions is unclear please use this as example to ask:

            • "Tell me everything about Saturn"
            • "How massive is Neptune?"
            • "Is Pluto in the list of planets?"
            • "How many moons does Earth have?"
            • "What moons does Mars have?"
            • "How far is Jupiter from the Sun?"
            • "List all planets"
            """
        return help_text
