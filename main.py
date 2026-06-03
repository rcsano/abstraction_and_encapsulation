RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"

from fan import Fan

def print_fan_dashboard(label, fan_obj):
    current_color = fan_obj.get_color().lower()
    theme = YELLOW if current_color == "yellow" else BLUE if current_color == "blue" else RESET

    status_text = f"{GREEN}ON{theme}" if fan_obj.is_on() else f"{RED}OFF{theme}"

    speed_names = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}

    print(f"{theme}{BOLD}=== {label.upper()} DASHBOARD ==={RESET}")
    print(f"{theme}STATUS : {status_text}")
    print(f"{theme}SPEED  : {WHITE}{speed_names.get(fan_obj.get_speed())}{RESET}")
    print(f"{theme}RADIUS : {WHITE}{fan_obj.get_radius()} mm{RESET}")
    print(f"{theme}COLOR  : {WHITE}{fan_obj.get_color().upper()}{RESET}")
    print(f"{theme}===================================\n")

def main():
    fan_one = Fan(Fan.FAST, 10.0, "yellow", True)
    fan_two = Fan(Fan.MEDIUM, 5.0, "blue", False)

    print_fan_dashboard("Fan Object 1", fan_one)
    print_fan_dashboard("Fan Object 2", fan_two)

if __name__ == "__main__":
    main()
