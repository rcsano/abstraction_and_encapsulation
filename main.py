# ANSI color constants
BOLD = "\033[1m"
WHITE = "\033[97m"
BLUE = "\033[94m"
RESET = "\033[0m"

# import pet class
from pet import Pet
import time

# instantiate pet object and accept keyboard inputs
def main():
    my_pet = Pet()

    print(f"{BLUE}{BOLD}===========================================")
    print("      PET REGISTRY PORTAL INITIALIZED")
    print(f"==========================================={RESET}")

    name_input = input(" -> Enter pet name: ")
    type_input = input(" -> Enter animal type: ")
    age_input = int(input(" -> Enter pet age: "))

    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)

    print(f"\n{WHITE}>>> PROCESSING DIGITAL IDENTIFICATION CARD...{RESET}")
    time.sleep(0.80)

    name_text = my_pet.get_name().upper()
    type_text = my_pet.get_animal_type().upper()
    age_text = f"{my_pet.get_age()} YEARS OLD"

# display pet data strings
    print(f"\n{BLUE}┌─────────────────────────────────────────┐")
    print(f"│         {BOLD}🐾 OFFICIAL PET RECORD{RESET}{BLUE}          │")
    print(f"├─────────────────────────────────────────┤")
    print(f"│  NAME   : {WHITE}{name_text:<29}{BLUE} │")
    print(f"│  SPECIES: {WHITE}{type_text:<29}{BLUE} │")
    print(f"│  AGE    : {WHITE}{age_text:<29}{BLUE} │")
    print(f"└─────────────────────────────────────────┘{RESET}")

    print(f"\n{WHITE}===========================================")
    print("   REGISTRATION SUCCESSFUL: RECORD SAVED")
    print(f"==========================================={RESET}\n")

if __name__ == "__main__":
    main()