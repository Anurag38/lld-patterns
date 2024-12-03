import heapq

class Elevator:
    def __init__(self, id, capacity):
        self.id = id
        self.current_floor = 0
        self.direction = "IDLE"  # "UP", "DOWN", or "IDLE"
        self.state = "IDLE"  # "IDLE", "MOVING", "STOPPED"
        self.capacity = capacity
        self.up_requests = []  # Min-heap for upward requests
        self.down_requests = []  # Max-heap for downward requests (negative values for sorting)

    def move(self):
        if self.direction == "UP" and self.up_requests:
            next_floor = heapq.heappop(self.up_requests)  # Get the nearest upward request
            self.current_floor = next_floor
            self.state = "STOPPED" if not self.up_requests else "MOVING"
        elif self.direction == "DOWN" and self.down_requests:
            next_floor = -heapq.heappop(self.down_requests)  # Get the nearest downward request
            self.current_floor = next_floor
            self.state = "STOPPED" if not self.down_requests else "MOVING"
        else:
            self.direction = "IDLE"
            self.state = "IDLE"

    def add_request(self, floor):
        if floor > self.current_floor:
            heapq.heappush(self.up_requests, floor)
        elif floor < self.current_floor:
            heapq.heappush(self.down_requests, -floor)
        self.update_direction()

    def update_direction(self):
        if self.direction == "IDLE":
            if self.up_requests:
                self.direction = "UP"
            elif self.down_requests:
                self.direction = "DOWN"

    def __str__(self):
        return (f"Elevator {self.id}: Floor {self.current_floor}, "
                f"Direction {self.direction}, Up: {self.up_requests}, Down: {[-x for x in self.down_requests]}")


class Request:
    def __init__(self, pickup_floor, dropoff_floor):
        # Create a request for moving from one floor to another
        self.pickup_floor = pickup_floor  # Floor where the request is made
        self.dropoff_floor = dropoff_floor  # Destination floor
        # Determine the direction of the request based on pickup and dropoff
        self.direction = "UP" if dropoff_floor > pickup_floor else "DOWN"


class ElevatorController:
    def __init__(self, num_elevators, capacity):
        self.elevators = [Elevator(i, capacity) for i in range(num_elevators)]
        self.requests_queue = []  # Global queue for unassigned requests

    def add_request(self, pickup_floor, dropoff_floor):
        best_elevator = self.find_best_elevator(pickup_floor)
        if best_elevator:
            best_elevator.add_request(pickup_floor)
            best_elevator.add_request(dropoff_floor)
        else:
            self.requests_queue.append((pickup_floor, dropoff_floor))

    def find_best_elevator(self, pickup_floor):
        # Prioritize IDLE elevators or elevators already moving in the request's direction
        best_elevator = None
        min_distance = float("inf")
        for elevator in self.elevators:
            if elevator.state == "IDLE":
                distance = abs(elevator.current_floor - pickup_floor)
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
            elif (elevator.direction == "UP" and pickup_floor > elevator.current_floor) or \
                 (elevator.direction == "DOWN" and pickup_floor < elevator.current_floor):
                distance = abs(elevator.current_floor - pickup_floor)
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
        return best_elevator

    def handle_starvation(self):
        # Promote old requests that have been waiting for too long
        for request in self.requests_queue:
            pickup_floor, dropoff_floor = request
            best_elevator = self.find_best_elevator(pickup_floor)
            if best_elevator:
                best_elevator.add_request(pickup_floor)
                best_elevator.add_request(dropoff_floor)
                self.requests_queue.remove(request)

    def step(self):
        self.handle_starvation()
        for elevator in self.elevators:
            elevator.move()

    def display_status(self):
        for elevator in self.elevators:
            print(elevator)
