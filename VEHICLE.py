from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    def __init__(self, speed, passenger_limit):
        self.speed = speed  # in km/h
        self.passenger_limit = passenger_limit  # in persons

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print(f"{self.__class__.__name__} is stopping.")

# Subclasses
class Car(Vehicle):
    def __init__(self, speed, passenger_limit, num_doors, fuel_type):
        super().__init__(speed, passenger_limit)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def start(self):
        print("Car: get_engine() called - Engine started")

    def honk(self):
        print("Car: honk() called - Beep beep!")

    def info(self):
        print(f"Car -> Speed: {self.speed} km/h, Passengers: {self.passenger_limit} persons, Doors: {self.num_doors}, Fuel: {self.fuel_type}")

class Bicycle(Vehicle):
    def __init__(self, speed, passenger_limit, num_gears, has_bell):
        super().__init__(speed, passenger_limit)
        self.num_gears = num_gears
        self.has_bell = has_bell

    def start(self):
        print("Bicycle: start() called - Pedaling...")

    def ring_bell(self):
        print("Bicycle: ring_bell() called - Ring ring!")

    def brake(self):
        print("Bicycle: brake() called - slowing down...")

    def info(self):
        print(f"Bicycle -> Speed: {self.speed} km/h, Passengers: {self.passenger_limit} persons, Gears: {self.num_gears}, Bell: {self.has_bell}")

class Motorcycle(Vehicle):
    def __init__(self, speed, passenger_limit, transmission_type, tire_type):
        super().__init__(speed, passenger_limit)
        self.transmission_type = transmission_type
        self.tire_type = tire_type

    def start(self):
        print("Motorcycle: rev_engine() called - Vroom!")

    def enable_abs(self):
        print("Motorcycle: enable_abs() called - ABS enabled")

    def info(self):
        print(f"Motorcycle -> Speed: {self.speed} km/h, Passengers: {self.passenger_limit} persons, Transmission: {self.transmission_type}, Tire: {self.tire_type}")

class Boat(Vehicle):
    def __init__(self, speed, passenger_limit, length, boat_type):
        super().__init__(speed, passenger_limit)
        self.length = length  # in meters
        self.boat_type = boat_type

    def start(self):
        print("Boat: lower_anchor() called - Anchor dropped")

    def raise_sail(self):
        print("Boat: raise_sail() called - Sail raised")

    def info(self):
        print(f"Boat -> Speed: {self.speed} knot, Passengers: {self.passenger_limit} persons, Length: {self.length} meters, Type: {self.boat_type}")

# Vehicle creation by user input
def create_vehicles():
    print("Enter Car details:")
    car = Car(
        int(input("Speed (km/h): ")),
        int(input("Passenger limit: ")),
        int(input("Number of doors: ")),
        input("Fuel type: ")
    )

    print("\nEnter Bicycle details:")
    bicycle = Bicycle(
        int(input("Speed (km/h): ")),
        int(input("Passenger limit: ")),
        int(input("Number of gears: ")),
        input("Has bell? (yes/no): ").lower() == "yes"
    )

    print("\nEnter Motorcycle details:")
    motorcycle = Motorcycle(
        int(input("Speed (km/h): ")),
        int(input("Passenger limit: ")),
        input("Transmission type: "),
        input("Tire type: ")
    )

    print("\nEnter Boat details:")
    boat = Boat(
        int(input("Speed (knot): ")),
        int(input("Passenger limit: ")),
        float(input("Length (meters): ")),
        input("Boat type: ")
    )

    return {
        "car": car,
        "bicycle": bicycle,
        "motorcycle": motorcycle,
        "boat": boat
    }

# Vehicle Menu Handler
class VehicleMenu:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def show_vehicle_info(self):
        print("\nVehicle Information:")
        self.vehicles["car"].info()
        self.vehicles["bicycle"].info()
        self.vehicles["motorcycle"].info()
        self.vehicles["boat"].info()

    def car_menu(self):
        car = self.vehicles["car"]
        while True:
            print("\nCar Options:\n1. Start\n2. Honk\n3. Stop\n4. Show Info\n5. Back")
            choice = input("Choose: ")
            if choice == '1':
                car.start()
            elif choice == '2':
                car.honk()
            elif choice == '3':
                car.stop()
            elif choice == '4':
                car.info()
            elif choice == '5':
                break

    def bicycle_menu(self):
        bike = self.vehicles["bicycle"]
        while True:
            print("\nBicycle Options:")
            print("1. Start")
            option_map = {"1": bike.start}
            option_num = 2

            if bike.has_bell:
                print(f"{option_num}. Ring Bell")
                option_map[str(option_num)] = bike.ring_bell
                option_num += 1

            print(f"{option_num}. Brake")
            option_map[str(option_num)] = bike.brake
            option_num += 1

            print(f"{option_num}. Stop")
            option_map[str(option_num)] = bike.stop
            option_num += 1

            print(f"{option_num}. Show Info")
            option_map[str(option_num)] = bike.info
            option_num += 1

            print(f"{option_num}. Back")
            back_option = str(option_num)

            choice = input("Choose: ")
            if choice in option_map:
                option_map[choice]()
            elif choice == back_option:
                break
            else:
                print("Invalid choice.")

    def motorcycle_menu(self):
        moto = self.vehicles["motorcycle"]
        while True:
            print("\nMotorcycle Options:\n1. Rev Engine\n2. Enable ABS\n3. Stop\n4. Show Info\n5. Back")
            choice = input("Choose: ")
            if choice == '1':
                moto.start()
            elif choice == '2':
                moto.enable_abs()
            elif choice == '3':
                moto.stop()
            elif choice == '4':
                moto.info()
            elif choice == '5':
                break

    def boat_menu(self):
        boat = self.vehicles["boat"]
        while True:
            print("\nBoat Options:\n1. Lower Anchor\n2. Raise Sail\n3. Stop\n4. Show Info\n5. Back")
            choice = input("Choose: ")
            if choice == '1':
                boat.start()
            elif choice == '2':
                boat.raise_sail()
            elif choice == '3':
                boat.stop()
            elif choice == '4':
                boat.info()
            elif choice == '5':
                break

    def main_menu(self):
        while True:
            print("\nMain Menu:\n1. Car\n2. Bicycle\n3. Motorcycle\n4. Boat\n5. Show All Info\n6. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.car_menu()
            elif choice == '2':
                self.bicycle_menu()
            elif choice == '3':
                self.motorcycle_menu()
            elif choice == '4':
                self.boat_menu()
            elif choice == '5':
                self.show_vehicle_info()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    vehicles = create_vehicles()
    menu = VehicleMenu(vehicles)
    menu.main_menu()
