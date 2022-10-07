'''Problema 1. GCD'''


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


arr = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    nr = int(input())
    arr.append(nr)

div = gcd(arr[0], arr[1])

for i in range(2, n):
    div = gcd(div, arr[i])

print(div)

'''Problema 2. Vowels'''

string = input("Enter a string: ")
string = string.lower()
nr_of_vowels = 0
vowels = "aeiou"


for i in range(0, len(string)):
    if vowels.find(string[i]) != -1:
        nr_of_vowels += 1


print(nr_of_vowels)

'''Problema 3. Number of occurrences of the first string in the second'''

string_1 = input("First string: ")
string_2 = input("Second string: ")

nr = string_2.count(string_1)

print(nr)



'''Problema 4. UpperCamelCase -> lowercase_with_underscores'''

txt = "UpperCamelCase"
new_txt = ''
new_txt = new_txt+txt[0].lower()
for i in range(1,len(txt)):
    if txt[i].isupper():
        new_txt = new_txt+ '_'
        new_txt = new_txt + (txt[i].lower())
    else:
        new_txt = new_txt + (txt[i])

print(new_txt)













