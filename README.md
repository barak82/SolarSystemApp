## ✅ Solar System Information System App Mandatory Requirements
## Usage Instructions

1. Run the program: `python main.py`
2. Select a planet from the dropdown or list
3. Click query buttons to get specific information
4. write your querry on the space to check if a planet exists
5. Results display in the text area below

### Data Types
- Planet names stored as strings
- Mass stored as floats 
- Distance stored as integers/floats
- Moons stored as lists of strings

### User Queries Supported
- "Tell me everything about [planet]" - Complete information display
- "How massive is [planet]" - Mass query
- "Is [planet] in the list" - check if the planet exists
- "How many moons does [planet] have" - Moon count

### Input Validation
- Validates planet selection before queries
- Handles non-existent planet names
- Case-insensitive matching
- User-friendly error messages

### Data Storage
- JSON file storage for planet data


### GUI Implementation
- Tkinter-based graphical interface
- user can select the planet and ask questions using the buttons or typing directly
- Planet selection via combobox and listbox


# Solar System Information System - Test Plan

## Test Objectives
- Verify all program functionality works correctly
- Ensure proper error handling
- Validate user input processing
- Test GUI components and user interactions
- Test natural language processing capabilities

## Test Environment
- Python 3.6+
- Tkinter library
- Unit test framework

## Test Cases

### 1. Data Model Tests
- [x] Test Planet object creation with valid data
- [x] Test Planet to dictionary conversion
- [x] Test Planet creation from dictionary
- [x] Test data deserialization

### 2. SolarSystemExecuter Tests
- [x] Test manager initialization with default data
- [x] Test loading data from file
- [x] Test saving data to file
- [x] Test retrieving planet by name (case-insensitive)
- [x] Test retrieving non-existent planet
- [x] Test getting all planet names
- [x] Test getting planet mass
- [x] Test getting planet distance
- [x] Test getting planet moons
- [x] Test getting moon count
- [x] Test checking planet existence

### 3. Processing Tests
- [x] Test "everything about" queries
- [x] Test mass queries
- [x] Test distance queries
