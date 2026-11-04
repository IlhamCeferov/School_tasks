import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(
            0,
            min(self.maximum_speed, self.current_speed + change),
        )

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume



if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(100)
    gasoline_car.accelerate(80)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(
        f"{electric_car.registration_number}: "
        f"{electric_car.travelled_distance} km"
    )
    print(
        f"{gasoline_car.registration_number}: "
        f"{gasoline_car.travelled_distance} km"
    )