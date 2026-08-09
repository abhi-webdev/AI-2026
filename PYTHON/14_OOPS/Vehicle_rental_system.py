
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"

class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

        Vehicle.total_vehicles += 1
        self._rental_price = 0

    def get_details(self):
        return f"{self.brand}, {self.model}, {self.engine.get_engine_info()}"

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price >= 0:
            self._rental_price = price
        else:
            raise ValueError("Rental price cannot be negative")


class Car(Vehicle):
    def __init__(self, brand, model, engine, seats):
        super().__init__(brand, model, engine)
        self.seats = seats

    def get_details(self):
        return f"{super().get_details()}, Seats: {self.seats}"

engine = Engine(150)

vehicle = Vehicle("Toyota", "Camry", engine)

vehicle.rental_price = 500

print(vehicle.get_details())
print(vehicle.rental_price)

print(vehicle.get_vehicle_type())

car = Car("Honda", "City", engine, 5)
car.rental_price = 800

print(car.get_details())
print(car.rental_price)

print(Vehicle.get_total_vehicles())