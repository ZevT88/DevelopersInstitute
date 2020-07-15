#Exercise #1
def greatest_number(): 
    num1 = int(input("A number:  "))
    num2 = int(input("Another number:  ")) 
    num3 = int(input("Last number:  "))
    nums = []
    nums.append(num1)
    nums.append(num2)
    nums.append(num3) 
    nums.sort()
    print(f"The biggest number is: {nums[-1]}")


# greatest_number() 


#Exercise #2 
def is_vowel(letter): 
    if 'aeiou'.count(letter) == 0: 
        print("consonant")
    
    else: 
        print("vowel")

# is_vowel('d')  


#Exercise #3 


def indexOfFirst(list1): 
    set1 = set(list1)
    for word in set1:
        print(f"the first insrence of {word} is at spot {list1.index(f'{word}')}")



# indexOfFirst(["world", "world", "hello", "bunny", "bunny"]) 


#Exercise 4 
def joinlists(list1, list2):
    string1 =  str(list1)
    string2 = str(list2)
    list3 = []
    list3.append(string1)
    list3.append(string2)
    print(list3)


# joinlists(["hello"], ["world"]) 


#Exercise #7
import random
randomnum = random.randint(1,9)
def func():
    if int(input("guess a number from 1 to 9:  "))  == randomnum:
        print("You got it!")
    else: 
        func()
# func()



#Exercise #8

# list1 = list(range(1, 100001))
# for num in list1:
#     print(num)




#Exercise #9

list2 = list(range(1,1000001))
print(max(list2))
print(min(list2))
print(sum(list2))