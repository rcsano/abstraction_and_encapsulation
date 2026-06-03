# import class from fan module
from fan import Fan

# show output menu or dashboard logic
def print_fan_dashboard(label, fan_obj):
    status = "ON" if fan_obj.is_on() else "OFF"
    speed_names = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}
    print(f"{label.upper()}\nSTATUS: {status}\nSPEED: {speed_names.get(fan_obj.speed())}")
    print(f"RADIUS: {fan_obj.get_radius()}\nCOLOR: {fan_obj.get_color()}\n")

# instantiate two fan objects with distinct values
def main():
    fan_one = Fan(Fan.FAST, 10.0, "yellow", True)
    fan_two = Fan(Fan.MEDIUM, 5.0, "blue", False)

# print result fields using getter methods
    print_fan_dashboard("Fan Object 1", fan_one)
    print_fan_dashboard("Fan Object 2", fan_two)

if __name__ == "__main__":
    main()
