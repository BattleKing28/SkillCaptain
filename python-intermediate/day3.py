class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand - {self.brand}\n Model - {self.model}")

    pass


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Load Capacity - {self.load_capacity}")


car1 = Vehicle("Tesla", "Model Y")
car1.display_info()
truck1 = Truck("Tesla", "CyberTruck", "5000 Kg")
truck1.display_info()
