class Elevator:
    def __init__(self, id, capacity):
        # Initialize an elevator with a unique ID and capacity
        self.id = id  # Unique identifier for the elevator
        self.current_floor = 0  # Start at the ground floor
        self.direction = "IDLE"  # Direction can be "UP", "DOWN", or "IDLE"
        self.state = "IDLE"  # State can be "IDLE", "MOVING", or "STOPPED"
        self.capacity = capacity  # Maximum capacity of the elevator
        self.requests = []  # List to store floor requests

    def move(self):
        # Moves the elevator towards its next request
        if self.requests:
            # Get the next requested floor
            next_floor = self.requests[0]
            if self.current_floor < next_floor:
                # Move up if the requested floor is above
                self.direction = "UP"
                self.current_floor += 1
            elif self.current_floor > next_floor:
                # Move down if the requested floor is below
                self.direction = "DOWN"
                self.current_floor -= 1
            else:
                # Arrive at the requested floor and stop
                self.requests.pop(0)  # Remove the completed request
                self.state = "STOPPED"  # Stop to open doors
                self.direction = "IDLE"  # Reset direction
        else:
            # No requests, the elevator is idle
            self.state = "IDLE"
            self.direction = "IDLE"

    def add_request(self, floor):
        # Adds a floor request to the elevator's queue
        if floor not in self.requests:
            self.requests.append(floor)  # Add the floor to the request list
            self.requests.sort()  # Sort requests for sequential handling

    def __str__(self):
        # String representation of the elevator's current state
        return f"Elevator {self.id}: Floor {self.current_floor}, Direction {self.direction}, Requests: {self.requests}"


class Request:
    def __init__(self, pickup_floor, dropoff_floor):
        # Create a request for moving from one floor to another
        self.pickup_floor = pickup_floor  # Floor where the request is made
        self.dropoff_floor = dropoff_floor  # Destination floor
        # Determine the direction of the request based on pickup and dropoff
        self.direction = "UP" if dropoff_floor > pickup_floor else "DOWN"


class ElevatorController:
    def __init__(self, num_elevators, capacity):
        # Initialize the controller with multiple elevators
        self.elevators = [Elevator(i, capacity) for i in range(num_elevators)]
        self.requests_queue = []  # Queue for unassigned requests

    def add_request(self, pickup_floor, dropoff_floor):
        # Add a new request to the system
        self.requests_queue.append(Request(pickup_floor, dropoff_floor))

    def assign_requests(self):
        # Assign unprocessed requests to the best available elevator
        for request in self.requests_queue:
            best_elevator = self.find_best_elevator(request)
            if best_elevator:
                # Add the request to the best elevator and remove it from the queue
                best_elevator.add_request(request.pickup_floor)
                best_elevator.add_request(request.dropoff_floor)
                self.requests_queue.remove(request)

    def find_best_elevator(self, request):
        # Find the most suitable elevator for a given request
        best_elevator = None
        min_distance = float("inf")  # Start with a large distance
        for elevator in self.elevators:
            # Check if the elevator is idle or moving in the same direction as the request
            if elevator.state == "IDLE" or elevator.direction == request.direction:
                # Calculate distance to the pickup floor
                distance = abs(elevator.current_floor - request.pickup_floor)
                if distance < min_distance:
                    # Update the best elevator if this one is closer
                    min_distance = distance
                    best_elevator = elevator
        return best_elevator  # Return the best elevator or None if no match

    def step(self):
        # Process one step of the simulation
        self.assign_requests()  # Assign requests to elevators
        for elevator in self.elevators:
            # Move each elevator towards its next request
            elevator.move()

    def display_status(self):
        # Display the status of all elevators
        for elevator in self.elevators:
            print(elevator)  # Print the string representation of each elevator
