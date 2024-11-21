class Transport:
    def calculate_cost(self, weight, distance):
        raise NotImplementedError("Subclasses must implement this method.")

class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return weight * 5 + distance * 2  # Example: $5 per kg + $2 per km

class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return weight * 2 + distance * 1  # Example: $2 per kg + $1 per km

class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return weight * 10 + distance * 5  # Example: $10 per kg + $5 per km

def calculate_delivery_costs(transports, weight, distance):
    for transport in transports:
        print(f"{transport.__class__.__name__} Delivery Cost: ${transport.calculate_cost(weight, distance)}")

# Example usage
truck = Truck()
ship = Ship()
plane = Plane()

transports = [truck, ship, plane]
calculate_delivery_costs(transports, weight=100, distance=50)
