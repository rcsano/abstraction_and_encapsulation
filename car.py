# get car details (make, year_model)
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__year_model = model
        self.__speed = 0

# create attributes with initial speed as 0
    def get_speed(self):
        return self.__speed

# perform acceleration (add 5 to speed)
    def accelerate(self):
        self.__speed += 5

# perform braking (subtract 5 from speed)
    def decelerate(self):
        if self.__speed > 0:
            self.__speed -= 5
        else:
            self.__speed = 0
