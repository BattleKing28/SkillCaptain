print("Please input number 1")
num1 = int(input())
print("Please input number 2")
num2 = int(input())

try:
    res = num1 / num2
except ZeroDivisionError as err:
    print(err)
else:
    print("Division of num1 and num2 = ", res)
finally:
    print("Last line of code")
