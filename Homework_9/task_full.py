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


if __name__ == "__main__":
    cars = [
        Car(f"ABC-{number}", random.randint(100, 200))
        for number in range(1, 11)
    ]

    while all(car.travelled_distance < 10_000 for car in cars):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    print(
        f"{'Registration':<15}"
        f"{'Max speed (km/h)':>18}"
        f"{'Current speed (km/h)':>23}"
        f"{'Distance (km)':>17}"
    )
    print("-" * 73)

    for car in cars:
        print(
            f"{car.registration_number:<15}"
            f"{car.maximum_speed:>18}"
            f"{car.current_speed:>23}"
            f"{car.travelled_distance:>17}"
        )