class SmartPhone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")

    def brand_info(self):
        return f"Brand: {self.brand}"
    
    def model_info(self):
        return f"Model: {self.model}"
    
    def check_storage(self):
        return f"Storage capacity is {self.storage} GB."
    
    # instances of the class
samsung = SmartPhone("Samsung", "Galaxy S21", 128)
iphone = SmartPhone("Apple", "iPhone 13", 256)
nokia = SmartPhone("Nokia", "3310", 16)
motorola = SmartPhone("Motorola", "Moto G Power", 64)

#using methods to display information about smart phones
samsung.display_info()
iphone.display_info()
nokia.display_info()

nokia.brand_info()
motorola.check_storage()

# using methods to get specific information about smart phones

print((samsung.brand_info()))
print((iphone.model_info()))
print((nokia.check_storage()))



# Activity 2: Polymorphism challenge
class Vehicles:
    def move(self):
        pass    # Abstract method

class Car(Vehicles):
    def move(self):
        return "car Drives."   # car attribute

class Plane(Vehicles):
    def move(self):
        return "plane flies."    # plane attribute

my_car = Car()
print(my_car.move()) 

my_plane = Plane()  
print(my_plane.move())  