class Farm():
    def __init__(self, farm_name): 
            self.farm_name = farm_name 
            self.animals = [] 
    def add_animals(self, new_animal, amount=1):
        for i in range(amount):
            self.animals.append(new_animal)
   
    
    def get_info(self): 
        once = set(self.animals)
        print(f"{self.farm_name}'s farm")  
        for i in once: 
            print(f"{i}  " +  "      " + f":{self.animals.count(f'{i}')}") 
        print("  E - I - E - I - O") 

    def get_animal_types(self): 
        once = set(self.animals)
        once2 = list(once)
        print(once2) 

    def get_short_info(self):
        once = set(self.animals)
        once2 = list(once)
        print(f"In {self.farm_name}'s farm there is {once2[0]}s, {once2[1]}, and {once2}s")

        
macdonald = Farm("Mcdonald") 
macdonald.add_animals('cow', 5)
macdonald.add_animals('sheep') 
macdonald.add_animals('sheep' ) 
macdonald.add_animals('goat', 12) 


macdonald.get_short_info()
