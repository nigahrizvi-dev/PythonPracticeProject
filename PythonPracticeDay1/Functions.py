# Simple function
def greet():
    print("Hello, welcome to Python!")

greet()
greet()


# Function with parameters
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# Function with a condition
def check_pass(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(check_pass(75))
print(check_pass(35))