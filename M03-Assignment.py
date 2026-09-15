
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type



class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# --- Main App ---
print("Please input  the details for your car.")


vehicle_type = "car"

year = input("Year: ")
make = input("Make: ")
model = input("Model: ")

# Validate doors
while True:
    doors = input("Number of doors (2 or 4): ")
    if doors in ("2", "4"):
        break
    print("Please enter either 2 or 4.")

# Validate roof type
while True:
    roof = input("Type of roof (solid or sun roof): ").lower()
    if roof in ("solid", "sun roof"):
        break
    print("Please enter 'solid' or 'sun roof'.")

# Create Automobile object
car = Automobile(vehicle_type, year, make, model, doors, roof)

# Output
print("\n--- Vehicle Information ---")
print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Number of doors: {car.doors}")
print(f"Type of roof: {car.roof}")
