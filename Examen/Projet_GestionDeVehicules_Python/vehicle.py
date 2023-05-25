class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_details(self):
        return f"Marque: {self.brand}, Modèle: {self.model}, Année: {self.year}, Couleur: {self.color}"

class Car(Vehicle):
    def __init__(self, brand, model, year, color, num_doors):
        super().__init__(brand, model, year, color)
        self.num_doors = num_doors

    def get_details(self):
        return f"{super().get_details()}, Nombre de portes: {self.num_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, num_wheels):
        super().__init__(brand, model, year, color)
        self.num_wheels = num_wheels

    def get_details(self):
        return f"{super().get_details()}, Nombre de roues: {self.num_wheels}"

class Bus(Vehicle):
    def __init__(self, brand, model, year, color, seating_capacity):
        super().__init__(brand, model, year, color)
        self.seating_capacity = seating_capacity

    def get_details(self):
        return f"{super().get_details()}, Capacité d'assise: {self.seating_capacity}"

class Metro(Vehicle):
    def __init__(self, brand, model, year, color, num_cars):
        super().__init__(brand, model, year, color)
        self.num_cars = num_cars

    def get_details(self):
        return f"{super().get_details()}, Nombre de voitures: {self.num_cars}"
