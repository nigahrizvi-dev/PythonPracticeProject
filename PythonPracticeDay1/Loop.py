##Printing even no.s from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

##Checking if a number is even or odd
user_input = int(input("Enter a number to check if it's even or odd"));
while (user_input != 0):
    if user_input%2==0:
        print(user_input, " is an even number.");
    else:
        print(user_input, " is an odd number.");