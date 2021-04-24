from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, _brand, _model, _color, _fuel, _condition, _mileage, car_type):
        super().__init__(_brand, _model, _color, _fuel, _condition, _mileage)
        self._car_type = car_type

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, car_type):
        self._car_type = car_type

    def status(self):
        print(f"""Brand: {self.brand} - Model: {self.model} - Color: {self.color} - Fuel: {self.fuel}
        Condition: {self.condition} - Mileage: {self.mileage:.0f}""")
