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
for i in range(1, len(txt)):
    if txt[i].isupper():
        new_txt = new_txt + '_'
        new_txt = new_txt + (txt[i].lower())
    else:
        new_txt = new_txt + (txt[i])

print(new_txt)

'''Problema 5. Matrix'''

A = [[1,  2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
n = 4
m = 4
r = 0
c = 0
i = 0
while r < m and c < n:
    for i in range(c, n):
        print(A[r][i], end=" ")
    r = r + 1
    for i in range(r, m):
        print(A[i][n - 1], end=" ")
    n = n - 1
    if (r < m):
        for i in range(n - 1, (c - 1), -1):
            print(A[m - 1][i], end=" ")
        m = m - 1
    if c < n:
        for i in range(m - 1, r - 1, -1):
            print(A[i][c], end=" ")
        c += 1

print("\n")


'''Problema 6. Palindrome'''

def palindrome(n):
    aux = n
    inv = 0
    while n > 0:
        digit = n % 10
        inv = inv * 10 + digit
        n = int(n / 10)
    if aux == inv:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")



n = int(input("Enter a number: "))
palindrome(n)


'''Problema 7. Extract number from text'''

def number_from_text(string):
    number = 0;
    for i in range(0, len(string)):
        while not string[i].isnumeric():
            i = i + 1
        if string[i].isnumeric():
            while string[i].isnumeric():
                number = number * 10 + int(string[i])
                i = i + 1
                if i > len(string) - 1:
                    break
            break
    print(number)

string = input("Enter a string: ")
number_from_text(string)

'''Problema 8. Decimal to binary'''

def decimal_to_binary(n):
    nr_de_biti = 0
    while n > 0:
        b = n % 2
        n = n // 2
        if b == 1:
            nr_de_biti = nr_de_biti + 1
    print(nr_de_biti)


n = int(input("Enter a number: "))
decimal_to_binary(n)

'''Problema 9. most common letter in a string'''

def most_common_letter(string):
    frecv = [0] * 150
    for i in range (0,len(string)):
        if string[i].isalpha:
            frecv[ord(string[i])] = frecv[ord(string[i])] + 1
    maxim = 0
    for i in range (65,123):
        if frecv[i] > maxim:
            maxim = frecv[i]
            caracter = chr(i)
    print(caracter)


string = input("Enter a string: ")
most_common_letter(string)

'''Problema 10. How many words in a text'''

#cuvintele sunt separate printr-un singur spatiu, deci e suficient sa numar doar spatiile + 1

def how_many_words(string):
    nr_of_words = 1
    for i in range (0,len(string)):
        if string[i] == ' ':
            nr_of_words = nr_of_words + 1
    print(nr_of_words)


string = input("Enter a string: ")
how_many_words(string)

