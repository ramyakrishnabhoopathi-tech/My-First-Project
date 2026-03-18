print("Hello GitHub")
name = "Ramya";
print("Hello", name)
def greet(name):
    print("Hello!", name)    

greet("Krishna")  

def add(a, b,c):
    return a + b +c       
result = add(5, 3, 2)
print("The sum is:", result)

def is_adult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
age = 20
status = is_adult(age)
print("The person is:", status)

def greet(name):
    print("Hello", name)

names = ["Ramya", "Sam", "Lee"]

for n in names:
    greet(n)

def square(number):
    return number * number

print(square(5))
print(square(10))

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)

numbers.append(6)
print(numbers)