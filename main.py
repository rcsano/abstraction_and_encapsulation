# import car class from module file
from car import Car

# instantiate car object
def main():
    my_vehicle = Car("2026", "Porsche 911 GT3 RS")
    print("Car simulation started.")

# sequence: acceleration (5 iterations)
    print("Accelerating:")
    for i in range(1, 6):
        my_vehicle.accelerate()
        print("Speed is now:", my_vehicle.get_speed(), "km/h")

# sequence: decelaration (5 iterations)
    print("Braking:")
    for i in range(1, 6):
        my_vehicle.brake()
        print("Speed is now:", my_vehicle.get_speed(), "km/h")

if __name__ == "__main__":
    main()