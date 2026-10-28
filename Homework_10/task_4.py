import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(0,min(self.maximum_speed, self.current_speed + change),)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n{self.name} - {self.distance} km")
        print(
            f"{'Registration':<15}"
            f"{'Max speed (km/h)':>18}"
            f"{'Current speed (km/h)':>23}"
            f"{'Distance (km)':>17}"
        )
        print("-" * 73)

        for car in self.cars:
            print(
                f"{car.registration_number:<15}"
                f"{car.maximum_speed:>18}"
                f"{car.current_speed:>23}"
                f"{car.travelled_distance:>17.1f}"
            )

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


if __name__ == "__main__":
    cars = [
        Car(f"ABC-{number}", random.randint(100, 200))
        for number in range(1, 11)
    ]

    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\nRace status after {hours} hours:")
            race.print_status()

    print(f"\nFinal race status after {hours} hours:")
    race.print_status()