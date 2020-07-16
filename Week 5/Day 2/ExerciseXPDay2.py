class Family():

    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **new_member):
        self.members.append(new_member)
        print(self.members)

    def over_18(self, name):
        for member in self.members:
            if member["name"] == name and member["age"] > 17:
                print(True)
                break
            else:
                print(False)
                break
    
    def __repr__(self):
        name_of_member = ""
        for member in self.members:
            name_of_member += member["name"] + " "
        return f"the names in the {self.last_name} family are: {name_of_member}"



# fam = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], last_name = "smith")
# fam.born(name = "chaim", age = 0, gender = "Male", is_child = True)
# fam.over_18('Michael')
# print(fam)



class TheIncredables(Family):
    
    def use_power(self,name):
        for member in self.members:
            if member["name"] == name and member["age"] > 18:
                print(member["power"])
                break
            else:
                raise ValueError("you have no power yet")

    def incredable_presentation(self):
        full_family = ""
        for member in self.members:
            full_family = member["incredable name"] + ":" + member["power"] + " "
            print(full_family)







incredables_family = TheIncredables([{"name": "Bob", "age": 40, "gender": "male", "is child": False, "power": "strength", "incredable name": "Mr Incredable"}, {"name": "Helen", "age": 37, "gender": "female", "is child": False, "power": "flexable", "incredable name": "Elastagirl"},{"name": "Dash", "age": 12, "gender": "male", "is child": True, "power": "speed", "incredable name": "speedy"}], last_name = "Parr") 
incredables_family.use_power("Bob")
incredables_family.incredable_presentation()