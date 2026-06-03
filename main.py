RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
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

    print(f"{theme}┌────────────────────────────────────────┐")
    print(f"│ ⚙️  {BOLD}{UNDERLINE}{label.upper()} METRICS DASHBOARD{RESET}{theme}     │")
    print(f"├────────────────────────────────────────┤")
    print(f"│  ⚡ STATUS : {status_text:<33}{theme}    │")
    print(f"│  📊 SPEED  : {WHITE}{speed_names.get(fan_obj.get_speed()):<26}{theme}│")
    print(f"│  📐 RADIUS : {WHITE}{str(fan_obj.get_radius()) + ' mm':<26}{theme}│")
    print(f"│  🎨 COLOR  : {WHITE}{fan_obj.get_color().upper():<26}{theme}│")
    print(f"└────────────────────────────────────────┘{RESET}\n")

def main():
    fan_one = Fan(Fan.FAST, 10.0, "yellow", True)
    fan_two = Fan(Fan.MEDIUM, 5.0, "blue", False)

    print_fan_dashboard("Fan Object 1", fan_one)
    print_fan_dashboard("Fan Object 2", fan_two)

if __name__ == "__main__":
    main()
