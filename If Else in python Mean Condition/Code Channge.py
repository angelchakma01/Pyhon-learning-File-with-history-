

# Inside the editor, complete the following steps:
# Create a variable age with the value 20
# Write an if statement that prints "Child" if age is less than 13
# Add an elif that prints "Teenager" if age is less than 18
# Add an else that prints "Adult"

# age = 20
# if age <= 13:
#     print("Child")
#     if age <=18:
#         print("Teenager")
#     else:
#         print("Adult")

print("This logic created by Angel Chakma")
results = input("Enter your results: ").strip().lower()

print("Enter input only passed or failed")

if results == "passed":
    print("Congratulations! You're passed.")

elif results == "failed":
    print("You failed, but remember one certificate can't change your life. so just move on and keep trying.")

else:
    print("Invalid input.")