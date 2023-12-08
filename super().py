class Human:
    def __init__(self, name, sex, age, etnic_group):
        self.name = name
        self.sex = sex
        self.age = age
        self.etnic_group = etnic_group

    def __repr__(self):
        if self.__class__.__name__ == "Women":
            return str(f"{self.name} can give birth to a child")
            
        
        if self.__class__.__name__ == "Men":
            return str(f"{self.name} can't give birth to a child")
            
        
        if self.__class__.__name__ == "Non_Binary":
            inp = input("Can you give birth to a child?")
            if inp == "yes":
                return str(f"{self.name} can give birth to a child")
            if inp == "no":
                return str(f"{self.name} can't give birth to a child")
        
         



class Women(Human):
    def __init__(self, name, sex, age, etnic_group):
        super().__init__(name, sex, age, etnic_group)

class Men(Human):
    def __init__(self, name, sex, age, etnic_group):
        super().__init__(name, sex, age, etnic_group)

class Non_Binary(Human):
    def __init__(self, name, sex, age, etnic_group):
        super().__init__(name, sex, age, etnic_group)




Andrew = Men("Andrew", "male", 11, "caucasian")
Ariana = Women("Ariana", "female", 25, "caucasian")
Selena = Non_Binary("Selena", "non binary", 31, "caucasian")

print(Andrew, "\n", Ariana, "\n", Selena)