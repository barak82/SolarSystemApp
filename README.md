## Solar System Information App
## Usage Instructions

1. Install packages based on the `requirements.txt`
2. Run the program: `python main.py`
2. Select a planet from the dropdown or list
3. Click query buttons to get specific information
4. write your querry on the space to check if a planet exists or any other query 
5. Results will be display in the text area below

### Data Types
- Planet names are represented as strings
- Mass is stored as floating-point numbers
- Distance is stored as integers or floats
- Moons are represented as lists of strings
### User Queries Supported
- "Tell me everything about [planet]" – Displays complete information about the planet
- "How massive is [planet]?" – Returns the mass of the specified planet
- "Is [planet] in the list?" – Checks for the planet's existence
- "How many moons does [planet] have?" – Returns the moon count

### Input Validation
- Ensures a valid planet is selected before processing queries
- Handles invalid or unknown planet names gracefully
- Matching is case-insensitive
- Provides clear and user-friendly error messages
### Data Storage
- Planet data is stored in a JSON file for persistence and easy modification


### GUI Implementation
- Built with Tkinter for a graphical user interface
- Users can select a planet and interact via buttons or by typing queries directly
- Planet selection is available through listbox

# Solar System Information System - Test Plan
## Test Environment
- Python 3.6+
- Tkinter library
- Unit test framework

## Test Objectives
- Ensure all features function as intended
- Validate robust error handling mechanisms
- Confirm accurate processing of user inputs
- Test all GUI components and interactions

## Test Cases

### 1. Data Model Tests
- [x] Test Planet object creation with valid data
- [x] Test Planet to dictionary conversion
- [x] Test Planet creation from dictionary
- [x] Test data deserialization

### 2. SolarSystemExecuter Tests
- [x] Test manager initialization with default data
- [x] Test loading data from file
- [x] Test retrieving planet by name 
- [x] Test retrieving non-existent planet
- [x] Test getting all planet names
- [x] Test getting planet mass
- [x] Test getting planet distance
- [x] Test getting planet moons
- [x] Test getting moon count