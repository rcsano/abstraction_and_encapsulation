# ANSI color constants
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# import car class from module file
from car import Car
import time

# instantiate car object
def main():
    my_vehicle = Car("2026", "Porsche 911 GT3 RS")

    print(f"{CYAN}{BOLD}==============================================")
    print("      VEHICLE PERFORMANCE MONITOR V1.0")
    print(f"=============================================={RESET}")
    print(f"BASELINE VELOCITY: {my_vehicle.get_speed()} KM/H\n")

# sequence: acceleration (5 iterations)
    print(f"{GREEN}{BOLD}[PHASE 01]: ACCELERATION SEQUENCE{RESET}")
    print("----------------------------------------------")
    for cycle in range(1, 6):
        time.sleep(0.20)
        my_vehicle.accelerate()
        print(f"LOG {cycle:02} | Current Velocity: {my_vehicle.get_speed()} KM/H")

# sequence: decelaration (5 iterations)
    print(f"\n{RED}{BOLD}[PHASE 02]: DECELERATION SEQUENCE{RESET}")
    print("----------------------------------------------")
    for cycle in range(1, 6):
        time.sleep(0.20)
        my_vehicle.decelerate()
        print(f"LOG {cycle:02} | Current Velocity: {my_vehicle.get_speed()} KM/H")

    print(f"\n{CYAN}==============================================")
    print("              SIMULATION COMPLETE                ")
    print(f"=============================================={RESET}")

if __name__ == "__main__":
    main()