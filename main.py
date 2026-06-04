# ANSI color constants
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# import car class from module file
from car import Car
import time

# added dashboard
def draw_cluster(phase_label, cycle, car_obj, color_theme):
    speed = car_obj.get_speed()

    gauge_bar = ("█" * speed) + ("░" * (25 - speed))

    print(f"{color_theme}┌──────────────────────────────────────────────────┐")
    print(f"│ {BOLD}{phase_label:<34} [LOG {cycle:02}] {RESET}{color_theme}     │")
    print(f"├──────────────────────────────────────────────────┤")
    print(f"│  MODEL  : {BOLD}PORSCHE 911 GT3 RS{RESET}{color_theme}                     │")
    print(f"│  VELO   : {BOLD}{speed:>3} KM/H{RESET}{color_theme}                               │")
    print(f"│  GAUGE  : {GREEN}[{gauge_bar}]{RESET}{color_theme}            │")
    print(f"└──────────────────────────────────────────────────┘{RESET}")

# instantiate car object
def main():
    my_vehicle = Car("2026", "Porsche 911 GT3 RS")

    print(f"{WHITE}{BOLD}INITIALIZING VEHICLE OPERATING SYSTEM")
    time.sleep(0.50)

# sequence: acceleration (5 iterations)
    print(f"\n{GREEN}EXECUTING ACCELERATION PROTOCOL{RESET}")
    for cycle in range(1, 6):
        time.sleep(0.20)
        my_vehicle.accelerate()
        draw_cluster("ACCELERATION PHASE", cycle, my_vehicle, GREEN)

# sequence: decelaration (5 iterations)
    print(f"\n{RED}EXECUTING BRAKING PROTOCOL{RESET}")
    for cycle in range(1, 6):
        time.sleep(0.20)
        my_vehicle.decelerate()
        draw_cluster("DECELERATION PHASE", cycle, my_vehicle, RED)

    print(f"\n{WHITE}{BOLD}SIMULATION TERMINATED. UNIT AT REST. :) {RESET}")

if __name__ == "__main__":
    main()