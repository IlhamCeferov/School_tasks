class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"The elevator is now on floor {self.current_floor}.")
        else:
            print("You are already on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"The elevator is now on floor {self.current_floor}.")
        else:
            print("You are already on the bottom floor.")

    def go_to_floor(self, floor):
        if not self.bottom_floor <= floor <= self.top_floor:
            print("Invalid floor number. Please choose a floor within the range.")
            return

        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for _ in range(number_of_elevators)
        ]

    def run_elevator(self, elevator_number, destination_floor):
        if not 1 <= elevator_number <= len(self.elevators):
            print("Invalid elevator number.")
            return

        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm activated! All elevators are going to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom_floor)


if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.fire_alarm()