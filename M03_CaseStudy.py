# Alex Hill
# M03_CaseStudy.py
# Presents a Vehicle class and an Automobile subclass to store details of a specific automobile
# uyear, umake, umodel, udoors and uroof are containers for user input
# ucar is instantiated using these values and the default value 'car' for type

class Vehicle():
    def __init__(self, type = "car"):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof, type = "car"):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

uyear = input("Enter the year: ")
umake = input("Enter the make: ")
umodel = input("Enter the model: ")
udoors = input("Enter the number of doors: ")
uroof = input("Enter the roof type: ")


ucar = Automobile(uyear, umake, umodel, udoors, uroof)
#ucar = Automobile(2014, "Ford", "Taurus", 4, "solid")

print("Vehicle type:", ucar.type)
print("Year:", ucar.year)
print("Make:", ucar.make)
print("Model:", ucar.model)
print("Number of doors:", ucar.doors)
print("Type of roof:", ucar.roof)