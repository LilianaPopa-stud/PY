import utils
import app

# ex. 1
print(utils.process_item(int(input("Enter a number: "))))
app.main()


# ex. 2
def my_function(*args, **kwargs):
    # sum of the values of the keyword arguments
    sum = 0
    for key in kwargs:
        sum += kwargs[key]
    return sum


suma = lambda *args, **kwargs: sum(kwargs.values())

print(suma(a=1, b=2, c=3))
print(my_function(1, b=2, c=3,d=4))

# ex. 3
def generate_vowels(string):
    vowels = []
    for char in string:
        if char in "aeiou":
            vowels.append(char)
    return vowels

print(generate_vowels("Programming in Python is fun"))

def generate_vowels2(string):
    return [char for char in string if char in "aeiou"]

print(generate_vowels2("Programming in Python is fun"))

def generate_vowels3(string):
    return list(filter(lambda x: x in "aeiou", string))

print(generate_vowels3("Programming in Python is fun"))

# ex. 5
def list_of_numbers(list):
    new_list = []
    for element in list:
        if type(element) == int:
            new_list.append(element)
    return new_list

print(list_of_numbers([1, "2", {1,2},"a", "b", "c",7]))

# ex. 6
def even_or_odd(list):
    even = []
    odd = []
    new_list = []
    for element in list:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    for i in range(0,len(odd)):
        new_list.append((even[i], odd[i]))
    return new_list


print(even_or_odd([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

