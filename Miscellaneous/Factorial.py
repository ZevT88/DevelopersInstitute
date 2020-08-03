from termcolor import colored
def Factorial(input_number):
    input_num = input_number
    num = input_num - 1 
    for i in range(num): 
        output = input_num * (num - i) 
        # time = colored(f"times {num - i} is", 'red')
        equals = colored("=", 'red')
        # print(f"{input_num:,d} {time} {output:,d}" )
        input_num = output 
    print(f"{input_number}! {equals} {input_num:,d}")





for i in range(1,100): 
    num = i + 1
    Factorial(num)



        

