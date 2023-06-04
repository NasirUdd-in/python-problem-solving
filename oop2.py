class Vehicle:
    def __init__(self, name, speed, mileage, seating_capacity):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("Vehicle Name:", self.name)
        print("Speed:", self.speed)
        print("Mileage:", self.mileage)

    def calculate_fare(self):
        fare = self.seating_capacity * 100
        return fare


class Bus(Vehicle):
    def calculate_fare(self):
        fare = super().calculate_fare()
        maintenance_charge = fare * 0.1
        total_fare = fare + maintenance_charge
        return total_fare


# Create an instance of the Bus class
bus = Bus("School Volvo", 180, 12, 50)

# Access the inherited methods from the parent class
bus.display_info()

# Calculate and print the fare for the bus instance
fare = bus.calculate_fare()
print("Total Fare:", fare)
