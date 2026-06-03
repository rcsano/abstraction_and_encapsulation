# ANSI color constants
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"

# import class from fan module
from fan import Fan

# show output menu or dashboard logic
def print_fan_dashboard(label, fan_obj):
    current_color = fan_obj.get_color().lower()
    theme = YELLOW if current_color == "yellow" else BLUE if current_color == "blue" else RESET

    status_text = f"{GREEN}ON{theme}" if fan_obj.is_on() else f"{RED}OFF{theme}"
    speed_names = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}

    header_title = f"⚙️  {label.upper()} METRICS"
    speed_text = f"{speed_names.get(fan_obj.get_speed())}"
    radius_text = f"{fan_obj.get_radius()} mm"
    color_text = f"{fan_obj.get_color().upper()}"

    print(f"{theme}┌──────────────────────────────────────┐")
    print(f"│{BOLD}{UNDERLINE}{header_title:<38}{RESET}{theme}│")
    print(f"├──────────────────────────────────────┤")
    print(f"│  ⚡ STATUS : {status_text:<34}{theme} │")
    print(f"│  📊 SPEED  : {WHITE}{speed_text:<23}{theme} │")
    print(f"│  📐 RADIUS : {WHITE}{radius_text:<23}{theme} │")
    print(f"│  🎨 COLOR  : {WHITE}{color_text:<23}{theme} │")
    print(f"└──────────────────────────────────────┘{RESET}\n")

# instantiate two fan objects with distinct values
def main():
    fan_one = Fan(Fan.FAST, 10.0, "yellow", True)
    fan_two = Fan(Fan.MEDIUM, 5.0, "blue", False)

# print result fields using getter method)
    print_fan_dashboard("Fan Object 1", fan_one)
    print_fan_dashboard("Fan Object 2", fan_two)

if __name__ == "__main__":
    main()
