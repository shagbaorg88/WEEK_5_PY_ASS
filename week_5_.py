class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self._brand = brand  # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._storage = storage  # Encapsulated attribute (in GB)
        self._battery_capacity = battery_capacity  # Encapsulated attribute (in mAh)
        self._battery_level = 100  # Encapsulated attribute (percentage)
        self._is_powered_on = False  # Encapsulated attribute
        
    # Getter methods for encapsulated attributes
    def get_brand(self):
        return self._brand
        
    def get_model(self):
        return self._model
        
    def get_storage(self):
        return self._storage
        
    def get_battery_capacity(self):
        return self._battery_capacity
        
    def get_battery_level(self):
        return self._battery_level
        
    def is_powered_on(self):
        return self._is_powered_on
        
    # Method to power on the phone
    def power_on(self):
        if self._battery_level > 5:
            self._is_powered_on = True
            print(f"{self._brand} {self._model} is now powered on.")
        else:
            print("Battery too low. Please charge first.")
            
    # Method to power off the phone
    def power_off(self):
        self._is_powered_on = False
        print(f"{self._brand} {self._model} is now powered off.")
        
    # Method to use the phone (drains battery)
    def use(self, minutes):
        if not self._is_powered_on:
            print("Cannot use phone while it's powered off.")
            return
            
        battery_drain = minutes * 0.5  # 0.5% per minute of use
        self._battery_level = max(0, self._battery_level - battery_drain)
        
        if self._battery_level <= 0:
            self._battery_level = 0
            self._is_powered_on = False
            print("Battery depleted. Phone has powered off.")
        else:
            print(f"Used phone for {minutes} minutes. Battery at {self._battery_level:.1f}%.")
            
    # Method to charge the phone
    def charge(self, minutes):
        if self._is_powered_on:
            print("Charging while powered on.")
            
        charge_amount = minutes * 0.8  # 0.8% per minute of charging
        self._battery_level = min(100, self._battery_level + charge_amount)
        print(f"Charged for {minutes} minutes. Battery at {self._battery_level:.1f}%.")
        
    # Method to display phone information
    def display_info(self):
        status = "On" if self._is_powered_on else "Off"
        print(f"{self._brand} {self._model} | {self._storage}GB | Battery: {self._battery_level:.1f}% | Status: {status}")


# Inheritance: GamingPhone extends Smartphone with additional features
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu_model, cooling_system):
        super().__init__(brand, model, storage, battery_capacity)
        self._gpu_model = gpu_model
        self._cooling_system = cooling_system
        self._is_gaming_mode = False
        
    # Method to activate gaming mode
    def activate_gaming_mode(self):
        if not self._is_powered_on:
            print("Cannot activate gaming mode while powered off.")
            return
            
        self._is_gaming_mode = True
        print(f"Gaming mode activated! {self._gpu_model} GPU is ready.")
        
    # Method to deactivate gaming mode
    def deactivate_gaming_mode(self):
        self._is_gaming_mode = False
        print("Gaming mode deactivated.")
        
    # Override the use method to account for gaming mode
    def use(self, minutes):
        if not self._is_powered_on:
            print("Cannot use phone while it's powered off.")
            return
            
        # Gaming mode drains battery faster
        drain_rate = 1.0 if self._is_gaming_mode else 0.5
        battery_drain = minutes * drain_rate
        self._battery_level = max(0, self._battery_level - battery_drain)
        
        if self._battery_level <= 0:
            self._battery_level = 0
            self._is_powered_on = False
            self._is_gaming_mode = False
            print("Battery depleted. Phone has powered off.")
        else:
            mode = " (Gaming Mode)" if self._is_gaming_mode else ""
            print(f"Used phone for {minutes} minutes{mode}. Battery at {self._battery_level:.1f}%.")
            
    # Override display_info to show gaming-specific info
    def display_info(self):
        status = "On" if self._is_powered_on else "Off"
        gaming_status = " | Gaming Mode: Active" if self._is_gaming_mode else ""
        print(f"{self._brand} {self._model} | {self._storage}GB | GPU: {self._gpu_model} | Battery: {self._battery_level:.1f}% | Status: {status}{gaming_status}")


# Demonstration
if __name__ == "__main__":
    print("=== Regular Smartphone ===")
    my_phone = Smartphone("Pear", "Phone 12", 128, 4000)
    my_phone.display_info()
    my_phone.power_on()
    my_phone.use(30)
    my_phone.charge(15)
    my_phone.display_info()
    
    print("\n=== Gaming Phone ===")
    my_gaming_phone = GamingPhone("Razer", "GameMaster", 256, 6000, "Adreno 650", "Vapor Chamber")
    my_gaming_phone.display_info()
    my_gaming_phone.power_on()
    my_gaming_phone.activate_gaming_mode()
    my_gaming_phone.use(30)  # Uses more battery in gaming mode
    my_gaming_phone.display_info()
    
    # Demonstrating polymorphism
    print("\n=== Polymorphism Example ===")
    phones = [my_phone, my_gaming_phone]
    
    for phone in phones:
        phone.use(15)  # Each phone type uses battery differently
        phone.display_info()
        print()