class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

my_car = Car()

my_car.start_engine()
my_car.stop_engine()
