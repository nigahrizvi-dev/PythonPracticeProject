print("Hello to GDG Team");
print("I have finlly started my Python journey");
print("I am checking the age eligibilty to join GDG Team");

name= input("Enter your name: ")
print("My name is", name);
age= int(input("Enter your age: "));
if (age >= 25):
    print("Your age is " + str(age) + ". You are eligible to join the data-science club");
elif (age < 25):
    print("You can join the general member position.");
else:
    print("You are not eligible to join the GDG Team.");

