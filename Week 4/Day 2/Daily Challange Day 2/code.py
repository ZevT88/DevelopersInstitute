


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
cypher = str(age1)[2]
b = "i" *  int(cypher)
print(f"        ___{b}___\n       |:H:a:p:p:y:| \n     __|___________|__ \n    |^^^^^^^^^^^^^^^^^|\n    |:B:i:r:t:h:d:a:y:| \n    |                 | \n    ~~~~~~~~~~~~~~~~~~~" ) 