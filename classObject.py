class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


# instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
your_car = Car("Toyota", "Hillux", 2024)

my_car.display_info()
your_car.display_info()