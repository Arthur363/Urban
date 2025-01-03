class Car:
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        return f"Model: {self.model}, Year: {self.year}, Engine: {self.engine}, Price: {self.price}, Mileage: {self.mileage}, Wheels: {self.wheels}"

class Truck(Car):
    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.wheels = 8

car1 = Car("ВАЗ 2101", 1970, 1.2, 100, 5000000)
print(car1.description())

truck1 = Truck("ЗИЛ 130", 1962, 6.0, 500, 7000000)
print(truck1.description())
