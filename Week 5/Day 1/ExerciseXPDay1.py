#Exercise #1
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

# cat1 = Cat("Bella", 7) 
# cat2 = Cat("Max", 10)  
# cat3 = Cat("Lucy", 4)

# def find_oldest(list1):  
#     list1.sort()
#     print("The oldest cat is " + f"{list1[-1::][0]}" + " years old")   
# find_oldest([cat1.age, cat2.age, cat3.age]) 

#Exercise 2 
    
# class Dog(): 
#     def __init__(self, nameDog, heightDog): 
#         self.namedog = nameDog 
#         self.heightDog = heightDog  
    
#     def talk(self): 
#         print("woof") 
    
#     def jump(self): 
#         height = self.heightDog
#         self.heightDog = height * 2 
#         print(self.heightDog)

 
# davids_dog = Dog("Rex", 50) 
# print(davids_dog.namedog) 
# print(davids_dog.heightDog)
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.namedog)
# print(sarahs_dog.heightDog) 


# def winner():  
#     if davids_dog.heightDog > sarahs_dog.heightDog: 
#         davids_dog.winner = True 
#         sarahs_dog.winner = False
#     else: 
#         davids_dog.winner = False 
#         sarahs_dog.winner = True


# winner()

# print(davids_dog.winner)
# print(sarahs_dog.winner)


#Exercise #3

# class Songs(): 
#     def __init__(self, lyrics): 
#         self.lyrics = lyrics
#     def sing_me_song(self):
#         lyrics = self.lyrics
#         for  i in lyrics: 
#             print(i)


# happy_bday = Songs(["Have a sunshine on you,", "Happy Birthday to you !"]) 

# happy_bday.sing_me_song()


#Exercise #4
class Zoo(): 
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name 
        self.animals = [] 
    def add_animal(self, new_animal): 
        self.animals.append(new_animal)
    def get_pen(self):
        for i in self.animals:
            print(i)

     
ramatGanSafari = Zoo("Ramat Gan Safari")
ramatGanSafari.add_animal("Tiger")
ramatGanSafari.add_animal("Baboon")
ramatGanSafari.add_animal("Bear")
ramatGanSafari.get_pen() 












