#ask user to enter number
number = int(input("Please enter a number: "))

#Find out if users number is divisible by 2 and 5
if number % 2==0 and number % 5==0:
    print(f"{number} is divisible by 2 and 5")
elif number % 2==0 or number % 5==0:
    print(f"{number} is divisible by 2 or 5")
else:
    print(f"{number} is not divisible by 2 and 5")


