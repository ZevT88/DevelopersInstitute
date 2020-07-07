


from datetime import date 
year1 = int(input("What is the Year you where born?  "))
month1 = int(input("What is the Month you where born?  ")) 
day1 = int(input("What is the Day you where born?  "))
mytuple =  (year1, month1,day1)
a, b, c = mytuple
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 

age1 = [(calculateAge(date(a, b, c)))] 
cypher = int(str(age1)[2])
b = "i" *  int(cypher)
side_cake = int((11 - cypher) / 2) * "_"

print(f"    {side_cake}{b}{side_cake}")
print("   |:H:A:P:P:Y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:I:R:T:H:D:a:Y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")
