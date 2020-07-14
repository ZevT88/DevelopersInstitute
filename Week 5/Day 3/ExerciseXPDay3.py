#Exercis 1 
# class Currency(): 
#     def __init__(self, value, currency_name): 
#         self.value = value
#         self.currency = currency_name 

#     def __repr__(self): 
#         return f"You have {self.value} {self.currency}"
    
#     def __str__(self): 
#         return f"You don't have {self.value} {self.currency}"  
    
#     def add(self, value, currency_name): 
#         if currency_name == self.currency: 
#             self.value = int(self.value) + int(value)
#         else: 
#             print("ERROR")

#     def subtract(self, value, currency_name): 
#         if currency_name == self.currency: 
#             self.value = int(self.value) - int(value)
#         else: 
#             print("ERROR") 
        
#     def devide(self, value, currency_name): 
#         if currency_name == self.currency: 
#             self.value = int(self.value) / int(value)
#         else: 
#             print("ERROR") 
    
#     def multiply(self, value, currency_name): 
#         if currency_name == self.currency: 
#             self.value = int(self.value) * int(value)
#         else: 
#             print("ERROR") 


# currency1 = Currency(10, "Dollars") 





#Exercise 2 
import math


class Circle(): 
    def __init__(self, radius):
        self.radius = radius
        self. diameter = radius * 2
        self.area = math.pi * self.radius ** 2 

    def __repr__(self): 
        return f"The circles Radius is {self.radius}, Diameter is {self.diameter} and the area is {self.area}"

    def find_area(self): 
        return self.area

    def add(self ,radius): 
        self.radius  += radius 
        self.diameter += radius * 2 
        self.area += math.pi * self.radius ** 2  
    
    def compare(self, radius): 
        if self.radius > radius: 
            print(f"Circle 1 is bigger with a radius of {self.radius}")
        elif self.radius == radius: 
            print("The 2 circles are Equal") 
        else: 
            print(f"Circle 2 is bigger with a radius of {radius}")

    def sort(self, *args):     
        circles = []
        circles.append(self.radius)
        for i in args:
            circles.append(i) 
        circles.sort() 
        print(circles)

c1 = Circle(5) 


