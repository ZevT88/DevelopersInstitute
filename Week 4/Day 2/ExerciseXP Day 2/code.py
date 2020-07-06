#Exercise #1 
# my_fav_numbers = set() 
# my_fav_numbers.add(8)
# my_fav_numbers.add(26)
# my_fav_numbers.add(11) 
# my_fav_numbers.add(7) 
# my_fav_numbers.remove(7) 
# friends_fav_numbers = set()
# friends_fav_numbers.add(3)
# friends_fav_numbers.add(9)
# my_fav_numbers.add(friends_fav_numbers)


#Exercise #2
# my_fav_numbers = (8,27)
# friends_fav_numbers = (11,7)
# fav_numbers = my_fav_numbers + friends_fav_numbers
# numbers = list(fav_numbers)
# numbers.remove(7)


#Exercise #3 

# A float is an integer with decimal points
# print(range(0,6,0.5))   


#Exercise #4  
# numbers = range(1,21) 
# for nums in numbers:
#     print(nums)



#Exercise #5 
# ask = ""
# pizza_toppings = set()
# while ask != "quit": 
#     ask = input('A pizza topping:   ')  
#     pizza_toppings.add(ask)  

# pizza_toppings.remove("quit")     
# print(pizza_toppings) 


# Exercise #6 

# ask = input("what is your age?  ")
# cost = [] 
# while ask != "done":  
#     if int(ask) > 3 and int(ask) < 13: 
#         cost.append(10) 
#     elif int(ask) > 12: 
#         cost.append(15)
#     else: 
#         cost.append(0)
#     ask = input("What is your age?   ")



# total_cost = sum(cost)
# print(f"Your total cost is: {total_cost}" ) 


#Exercise #7 
# names = ["bob", "joe", "fred", "jeff"] 
# for name in names:
#     age = input(f"what is {name}'s age?   ") 
#     if int(age) < 17: 
#         names.remove(f"{name}")  
    
# print(names) 


#Exercise #8 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"] 
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)


#Exercise #9 
# num = -1
# colors = ["Red", "Green", "Orange", "Pink", "Blue", "Yellow" ]
# while num < 5:
#     num = num + 1
#     print(colors[num]) 
