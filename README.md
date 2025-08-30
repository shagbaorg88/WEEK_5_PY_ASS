# README for Smartphone Class Implementation

## Overview
This Python program demonstrates object-oriented programming concepts including classes, inheritance, polymorphism, and encapsulation through a `Smartphone` class and its specialized subclass `GamingPhone`.

## Class Structure

### Smartphone Class
The base class representing a generic smartphone with the following features:

**Attributes:**
- `_brand`: Smartphone manufacturer (encapsulated)
- `_model`: Smartphone model (encapsulated)
- `_storage`: Storage capacity in GB (encapsulated)
- `_battery_capacity`: Battery capacity in mAh (encapsulated)
- `_battery_level`: Current battery level percentage (encapsulated)
- `_is_powered_on`: Power status (encapsulated)

**Methods:**
- `get_brand()`, `get_model()`, etc.: Getter methods for encapsulated attributes
- `power_on()`: Powers on the smartphone if battery level is sufficient
- `power_off()`: Powers off the smartphone
- `use(minutes)`: Simulates phone usage, draining the battery
- `charge(minutes)`: Simulates charging the phone
- `display_info()`: Displays phone information

### GamingPhone Class (Inherits from Smartphone)
A specialized smartphone class with gaming-specific features:

**Additional Attributes:**
- `_gpu_model`: GPU model information
- `_cooling_system`: Type of cooling system
- `_is_gaming_mode`: Gaming mode status

**Additional/Overridden Methods:**
- `activate_gaming_mode()`: Activates gaming mode
- `deactivate_gaming_mode()`: Deactivates gaming mode
- `use(minutes)`: Overridden to account for increased battery drain in gaming mode
- `display_info()`: Overridden to show gaming-specific information

## Key OOP Concepts Demonstrated

1. **Encapsulation**: All attributes are prefixed with `_` to indicate they're protected, and accessed via getter methods.

2. **Inheritance**: `GamingPhone` extends the `Smartphone` class, inheriting its attributes and methods.

3. **Polymorphism**: Both classes implement `use()` and `display_info()` methods, but they behave differently based on the specific phone type.

4. **Constructor Usage**: Each object is initialized with unique values through constructor parameters.

## How to Run

1. Save the code to a file (e.g., `smartphone.py`)
2. Run the program: `python smartphone.py`
3. The program will demonstrate:
   - Regular smartphone functionality
   - Gaming phone functionality with specialized features
   - Polymorphism by treating different phone types through a common interface

## Example Output
```
=== Regular Smartphone ===
Pear Phone 12 | 128GB | Battery: 100.0% | Status: Off
Pear Phone 12 is now powered on.
Used phone for 30 minutes. Battery at 85.0%.
Charged for 15 minutes. Battery at 97.0%.
Pear Phone 12 | 128GB | Battery: 97.0% | Status: On

=== Gaming Phone ===
Razer GameMaster | 256GB | GPU: Adreno 650 | Battery: 100.0% | Status: Off
Razer GameMaster is now powered on.
Gaming mode activated! Adreno 650 GPU is ready.
Used phone for 30 minutes (Gaming Mode). Battery at 70.0%.
Razer GameMaster | 256GB | GPU: Adreno 650 | Battery: 70.0% | Status: On | Gaming Mode: Active

=== Polymorphism Example ===
Used phone for 15 minutes. Battery at 89.5%.
Pear Phone 12 | 128GB | Battery: 89.5% | Status: On

Used phone for 15 minutes (Gaming Mode). Battery at 55.0%.
Razer GameMaster | 256GB | GPU: Adreno 650 | Battery: 55.0% | Status: On | Gaming Mode: Active
```

## Extending the Code
You can extend this implementation by:
1. Adding more smartphone subclasses (e.g., `BusinessPhone`, `CameraPhone`)
2. Implementing additional features like apps, calls, or messages
3. Adding more battery usage scenarios
4. Implementing a more sophisticated battery model

---

# README for Polymorphism Challenge: Animals and Vehicles

## Overview
This Python program demonstrates polymorphism through animal and vehicle hierarchies. Each class implements a `move()` method differently, showing how objects of different types can be treated uniformly through a common interface.

## Class Structure

### Animal Hierarchy

**Base Class: Animal**
- Attributes: `name`
- Methods: `move()`, `speak()`

**Subclasses:**
- `Dog`: Implements `move()` as running and `speak()` as barking
- `Bird`: Implements `move()` as flying and `speak()` as chirping
- `Fish`: Implements `move()` as swimming and `speak()` as bubbling
- `Snake`: Implements `move()` as slithering and `speak()` as hissing

### Vehicle Hierarchy

**Base Class: Vehicle**
- Attributes: `brand`, `model`
- Methods: `move()`, `fuel_type()`

**Subclasses:**
- `Car`: Implements `move()` as driving and `fuel_type()` as gasoline/diesel
- `Plane`: Implements `move()` as flying and `fuel_type()` as jet fuel
- `Boat`: Implements `move()` as sailing and `fuel_type()` as diesel/gasoline
- `Bicycle`: Implements `move()` as pedaling and `fuel_type()` as human power

## Key OOP Concepts Demonstrated

1. **Polymorphism**: All classes implement a `move()` method, but each behaves differently based on the specific type of object.

2. **Inheritance**: All animal classes inherit from the `Animal` base class, and all vehicle classes inherit from the `Vehicle` base class.

3. **Abstraction**: Base classes define method signatures that subclasses must implement.

4. **Type Checking**: The program demonstrates how to check object types to call appropriate methods (`isinstance()` checks).

## How to Run

1. Save the code to a file (e.g., `polymorphism_challenge.py`)
2. Run the program: `python polymorphism_challenge.py`
3. The program will demonstrate:
   - Different movement behaviors for animals
   - Different movement behaviors for vehicles
   - Additional information specific to each type
   - Mixed processing of animals and vehicles through polymorphism

## Example Output
```
=== Movement Demonstration ===
Buddy the Golden Retriever is running! 🐕
Tweety the Canary is flying! 🕊️
Nemo the Clownfish is swimming! 🐠
Slither the Python is slithering! 🐍

=== Movement Demonstration ===
Red Toyota Camry is driving on the road! 🚗
Delta Airlines's Boeing 737 is flying in the sky! ✈️
Yamaha 242 sport boat is sailing on water! ⛵
Trek FX hybrid bicycle is being pedaled on the path! 🚴

=== Additional Information ===
Buddy: Woof! Woof!
Tweety: Chirp! Chirp!
Nemo: Blub! Blub!
Slither: Hiss! Hiss!

=== Additional Information ===
Toyota Camry: Uses Gasoline or Diesel
Boeing 737: Uses Jet fuel
Yamaha 242: Uses Diesel or Gasoline
Trek FX: Uses Human power

=== Mixed Animals and Vehicles ===
Buddy the Golden Retriever is running! 🐕
Tweety the Canary is flying! 🕊️
Nemo the Clownfish is swimming! 🐠
Slither the Python is slithering! 🐍
Red Toyota Camry is driving on the road! 🚗
Delta Airlines's Boeing 737 is flying in the sky! ✈️
Yamaha 242 sport boat is sailing on water! ⛵
Trek FX hybrid bicycle is being pedaled on the path! 🚴
```

## Extending the Code
You can extend this implementation by:
1. Adding more animal or vehicle subclasses
2. Implementing additional common methods across hierarchies
3. Creating more complex behaviors and interactions
4. Adding user input to create objects dynamically
5. Implementing interfaces that cross the animal/vehicle boundary

## Learning Objectives
- Understand how polymorphism allows different objects to respond to the same method call in different ways
- Learn how to design class hierarchies with appropriate inheritance
- Practice implementing method overriding in subclasses
- See how type checking can be used to handle objects differently based on their type
