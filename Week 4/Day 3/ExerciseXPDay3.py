#Exercise #1
# numnames = { 
#     'ten' : 10,
#     'twenty': 20,
#     'thirty' : 30
# } 


#Exercise #2 
# store = { 

#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio, Ortega Gaona',
#     'type_of_clothes': 'men, women, children, home',
#     'international_competitors': 'Gap, H&M, Benetton',
#     'number_stores': 7000,
#     'major_color': 'France -> blue, Spain -> red, US -> pink, green',
#     'country_creation': 'spain'
# } 
# store2 = { 
#     'number_stores': 2
# } 
# store.update(store2) 

# if 'international_competitors' in store:
#         store['Desigual'] = ""

# store.pop("creation_date") 


# print(store['international_competitors'][4:8])

# print(len(store))

# print(store.keys()) 

 
# more_on_zara = { 
#     'creation_date': 1975,
#      'number_stores': 10000

#  }
 

# store.update(more_on_zara)

# print(store['number_stores'])


#Exercise 3

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
a = -1
disney_usersA = {}
for name in users: 
    disney_usersA.add({name: a})
    a + 1

print(disney_usersA) 