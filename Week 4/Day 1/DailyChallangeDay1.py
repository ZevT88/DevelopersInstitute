string = input("10 Characters please:  ") 

total = len(string)

if total < 10: 
    print("Thats too short")

if total > 10: 
    print("Thats too long")


# print (string[0])
# print (string[9])


# for i in range(len(string) + 1):
#     i + 1
#     print(string[:i]) 

import random
shuffled = list(string)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print (shuffled)