class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def display_info(self):
        print("Vehicle Name:", self.name)
        print("Speed:", self.speed)
        print("Mileage:", self.mileage)


class Bus(Vehicle):
    pass


# Create an instance of the Bus class
bus = Bus("School Volvo", 180, 12)

# Access the inherited method from the parent class
bus.display_info()
