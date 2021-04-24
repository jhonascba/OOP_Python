class Vehicle:
    def __init__(self, brand, model, color, fuel, condition, mileage):
        self._brand = brand
        self._model = model
        self._color = color
        self._fuel = fuel
        self._condition = condition

        if self._condition == 'New':
            self._mileage = 0
        else:
            self._condition = condition
            self._mileage = mileage

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        self._fuel = fuel

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, condition):
        self._condition = condition

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage
