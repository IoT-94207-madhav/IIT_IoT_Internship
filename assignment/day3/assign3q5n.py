
def greet(name, message="Good Morning"):
    print(message, name)

print("---- Default Parameters ----")
greet("Madhav")                 # uses default value
greet("Madhav", "Good Evening") # overrides default

def student_info(name, age, course):
    print("\nName :", name)
    print("Age  :", age)
    print("Course :", course)

print("\n---- Keyword Arguments ----")
student_info(age=20, course="Python", name="Amit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    return operation(x, y)

print("\n---- Function Passing ----")
print("Addition :", calculate(add, 10, 5))
print("Subtraction :", calculate(subtract, 10, 5))
