# import pet class
from pet import Pet

# instantiate pet object and accept keyboard inputs
def main():
    my_pet = Pet()

    print("Pet Registry System")
    name_input = input("Enter pet name: ")
    type_input = input("Enter animal type: ")
    age_input = int(input("Enter pet age: "))

    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)

# display pet data strings
    print("\nRegistered Data:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

if __name__ == "__main__":
    main()