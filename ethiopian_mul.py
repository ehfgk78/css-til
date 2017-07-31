# Ethiopian Multiplication

numbers = str(input("Tow numbers with comma like '132, 76':  ")).split(",")

result = 0
num1 = int(numbers[0])
num2 = int(numbers[1])

while num1 >= 1:
    if num1 % 2 == 0: print(num1, num2, "버려")
    else: print(num1, num2, "더해"); result = result + num2
    num1 = num1 //2
    num2 = num2 * 2

print("Result : ", result)
