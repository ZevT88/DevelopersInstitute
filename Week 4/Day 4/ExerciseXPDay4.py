#Exercise #1 
# def display_message(): 
#     print("In this chapter we are learning about functions") 
# print(display_message())

#Exercise #2 
# def favorite_book(title): 
#     print("my favorite book is" + title) 

# print(favorite_book("Harry Potter"))  


#Exercise #3
# def make_shirt(size, text): 
   
#     if size == "large":
#         print("The shirt is size " + size + 'and on it says "I love Python"')
#     elif size == "medium": 
#         print("The shirt is size " + size + 'and on it says "Pythons OK"')

#     else: 
#          print("The shirt is size " + size + "and on it says" + text)



# print(make_shirt("medium", "Hello world"))


#Exercise #4
# magicians = ["Bob", "Joe", "Harry", "Fred","Steve"]
# def show_magicians():
#     for names in magicians: 
#         print(names)

# def make_great(): 
#     for names in magicians: 
#         print(names + " is Great")



# print(make_great())  


#Exeecise #5 
# def describe_city(city, Country): 
#     if city == "Tokyo":
#         print(city + " is in" + " Japan")
#     elif city == "Beijing":  
#         print(city + " is in" + " Japan")
#     elif city == "Washington": 
#          print(city + " is in" + " United States")
#     elif city == "London":
#          print(city + "is in" + "England")
#     else: 
#         print("I don't know what country " + city + " is in" )
        

# print(describe_city("Tokyo", "")) 


# Exercise #6
from datetime import date
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 


def get_age(birtdate):
    currentAge = (calculateAge(date(int(birtdate[0:4]), int(birtdate[5:7]) ,  int(birtdate[8:10])))) 
    return currentAge

def can_retire(gender, date_of_birth): 
    current_age = get_age(date_of_birth) 
    if gender == "m" and current_age >= 67:  
        print("true") 
    elif gender == "f" and current_age >= 62: 
        print("true") 
    else: 
        print("false")
     
print(get_age("1958/03/12"))
print(can_retire("f","1958/03/12")) 



