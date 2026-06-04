# create pet class with encapsulation rules
class Pet:
    def __init__(self):
        # attributes: __name, __animal_type, __age
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

# mutator methods
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

# accessor methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age