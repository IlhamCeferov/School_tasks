class Airplane:
    def __init__(self, name, max_fuel_capacity, current_fuel):
        self.name = name
        self.max_fuel_capacity = max_fuel_capacity
        self.current_fuel = current_fuel

    def print_info(self):
        print(f"Airplane: {self.name}, Fuel: {self.current_fuel}/{self.max_fuel_capacity}")

class Airport:
    def __init__(self, name):
        self.name = name
        self.airplanes = []

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)

    def refuel(self, airplane):
        print(f"Refueling {airplane.name}")
        airplane.current_fuel = airplane.max_fuel_capacity

    def print_airplanes(self):
        print(f"Airplanes at {self.name} Airport")
        if not self.airplanes:
            print("No airplanes at the airport.")
        for airplane in self.airplanes:
            airplane.print_info()


if __name__ == "__main__":
    plane1 = Airplane("Boeing 747", 22000, 5000)
    plane2 = Airplane("Airbus 380", 20000, 12000)

    print("-Testing airplane info printing-")
    plane1.print_info()
    plane2.print_info()

    airport = Airport("Helsinki")
    airport.add_airplane(plane1)
    airport.add_airplane(plane2)
    airport.print_airplanes()
    airport.refuel(plane1)
    airport.print_airplanes()
