class  Suhas:
    current_year = 2024
    def __init__(self, name, age = 25, weight = 77) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        

obj = Suhas("suhas")
obj.current_year = 2025

print(f" current year : {obj.current_year} name :{obj.name} age :{ obj.age} weight :{obj.weight}")
print(obj.__getattribute__)