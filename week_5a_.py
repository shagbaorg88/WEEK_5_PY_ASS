# Base class for all animals
class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        pass  # To be implemented by subclasses
        
    def speak(self):
        pass  # To be implemented by subclasses

# Base class for all vehicles
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        pass  # To be implemented by subclasses
        
    def fuel_type(self):
        pass  # To be implemented by subclasses

# Animal subclasses
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def move(self):
        return f"{self.name} the {self.breed} is running! 🐕"
        
    def speak(self):
        return "Woof! Woof!"

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
        
    def move(self):
        return f"{self.name} the {self.species} is flying! 🕊️"
        
    def speak(self):
        return "Chirp! Chirp!"

class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
        
    def move(self):
        return f"{self.name} the {self.species} is swimming! 🐠"
        
    def speak(self):
        return "Blub! Blub!"

class Snake(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
        
    def move(self):
        return f"{self.name} the {self.species} is slithering! 🐍"
        
    def speak(self):
        return "Hiss! Hiss!"

# Vehicle subclasses
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color
        
    def move(self):
        return f"{self.color} {self.brand} {self.model} is driving on the road! 🚗"
        
    def fuel_type(self):
        return "Gasoline or Diesel"

class Plane(Vehicle):
    def __init__(self, brand, model, airline):
        super().__init__(brand, model)
        self.airline = airline
        
    def move(self):
        return f"{self.airline}'s {self.brand} {self.model} is flying in the sky! ✈️"
        
    def fuel_type(self):
        return "Jet fuel"

class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type
        
    def move(self):
        return f"{self.brand} {self.model} {self.boat_type} is sailing on water! ⛵"
        
    def fuel_type(self):
        return "Diesel or Gasoline"

class Bicycle(Vehicle):
    def __init__(self, brand, model, bicycle_type):
        super().__init__(brand, model)
        self.bicycle_type = bicycle_type
        
    def move(self):
        return f"{self.brand} {self.model} {self.bicycle_type} bicycle is being pedaled on the path! 🚴"
        
    def fuel_type(self):
        return "Human power"

# Function to demonstrate polymorphism
def demonstrate_movement(objects):
    print("=== Movement Demonstration ===")
    for obj in objects:
        print(obj.move())
    print()

# Function to show additional information based on type
def show_additional_info(objects):
    print("=== Additional Information ===")
    for obj in objects:
        if isinstance(obj, Animal):
            print(f"{obj.name}: {obj.speak()}")
        elif isinstance(obj, Vehicle):
            print(f"{obj.brand} {obj.model}: Uses {obj.fuel_type()}")
    print()

# Main program
if __name__ == "__main__":
    # Create various animals
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Bird("Tweety", "Canary"),
        Fish("Nemo", "Clownfish"),
        Snake("Slither", "Python")
    ]
    
    # Create various vehicles
    vehicles = [
        Car("Toyota", "Camry", "Red"),
        Plane("Boeing", "737", "Delta Airlines"),
        Boat("Yamaha", "242", "sport boat"),
        Bicycle("Trek", "FX", "hybrid")
    ]
    
    # Demonstrate polymorphism with animals
    demonstrate_movement(animals)
    
    # Demonstrate polymorphism with vehicles
    demonstrate_movement(vehicles)
    
    # Show additional information
    show_additional_info(animals)
    show_additional_info(vehicles)
    
    # Mix animals and vehicles to show true polymorphism
    print("=== Mixed Animals and Vehicles ===")
    mixed_objects = animals + vehicles
    for obj in mixed_objects:
        print(obj.move())