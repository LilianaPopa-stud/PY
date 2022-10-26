import math

'''Problema 1. fibonacci'''

number_of_terms = int(input("Enter the number of terms: "))
def fib(number_of_terms):
    if number_of_terms <= 0:
        return
    n2 = 1
    n1 = 0
    count = 0
    print("Fibonacci sequence: ")
    while count < number_of_terms:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count = count + 1
    print("\n")

fib(number_of_terms)


'''Problema 2. Prime numbers'''
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_numbers(list_of_numbers):
    list_of_prime_numbers = []
    for element in list_of_numbers:
        if prime(element) == True:
            list.append(list_of_prime_numbers,element)
    return list_of_prime_numbers


list_of_primes = prime_numbers([1,2,3,10,9,7,101,17,18,27,23,11,0,19])
print("Primes: ", list_of_primes, end="\n\n")

'''Problema 3. a intersected with b, a reunited with b, a - b, b - a'''

class Lists:
    def __init__(self):
        self.a_intersected_with_b = []
        self.a_reunited_with_b = []
        self.a_minus_b = []
        self.b_minus_a = []
        self.list_A = []
        self.list_B = []

def create_new_lists(list_a,list_b):
    L = Lists()

    list_a = list(dict.fromkeys(list_a))
    list_b = list(dict.fromkeys(list_b))
    L.list_A = list_a.copy()
    L.list_B = list_b.copy()

    # intersectie
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                list.append(L.a_intersected_with_b,element_a)

    # reuniune
    L.a_reunited_with_b = list_a.copy()
    copie_b = list_b.copy()
    for element_a in list_a:
        for element_b in copie_b:
            if element_a == element_b:
                copie_b.remove(element_a)
    L.a_reunited_with_b.extend(copie_b)

    # a minus b
    copie_a = list_a.copy()
    for i in range(0,len(list_a)):
        for j in range(0,len(list_b)):
            if list_a[i] == list_b[j]:
                copie_a.remove(list_a[i])
    L.a_minus_b = copie_a.copy()

    # b minus a
    copie_b = list_b.copy()
    for i in range(0,len(list_b)):
        for j in range(0,len(list_a)):
            if list_b[i] == list_a[j]:
                copie_b.remove(list_b[i])
    L.b_minus_a = copie_b.copy()
    return L

L = create_new_lists([1,2,2,2,2,3,4,20,19,18],[4,2,5,1,2,82,16,19,38])

print("List A: ", L.list_A)
print("List B: ", L.list_B)
print("A interesected with B: ", L.a_intersected_with_b)
print("A reunited with B: ", L.a_reunited_with_b)
print("A minus B: ", L.a_minus_b)
print("B minus A: ", L.b_minus_a,end="\n\n")

'''Problema 4. Compose'''

def compose(notes,moves,start_position):
    song = []
    song.append(notes[start_position])
    current_position = start_position
    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2), end="\n\n")

'''Problema 5. 0 under the main diagonal'''

def replace_with_zeros(matrix,rows,columns):
    if rows != columns:
        print("Nu este matrice patratica!")
        return
    for row in range(0, rows):
        for column in range(0,columns):
            if  row > column:
                matrix[row][column] = 0
    return matrix


matrix = replace_with_zeros([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]], 4, 4)
for i in range(0,4):
    print(matrix[i])
print("\n")

'''Problema 6. lists'''

def x_times(lists,x):
    number_of_lists = len(lists)
    concatenated_lists = []
    new_list = []
    for i in range(0,number_of_lists):
        for j in range(0,len(lists[i])):
            concatenated_lists.append(lists[i][j])
    for element in concatenated_lists:
        if concatenated_lists.count(element) == x:
            new_list.append(element)
    new_list = list(dict.fromkeys(new_list))
    return new_list


print("x_times: ", x_times([[1,2,22,1,5,3,12,8,5,5,],[2,2,2,2],[11,22,22,33],[11,1,2,6,7,4,5]],6),end="\n\n")


'''Problema 7: '''
def palindrome(n):
    aux = n
    inv = 0
    while n > 0:
        digit = n % 10
        inv = inv * 10 + digit
        n = int(n / 10)
    if aux == inv:
        return True
    else:
        return False


def create_tuple(list_of_integers):
    count = 0
    greatest = 0
    for element in list_of_integers:
        if palindrome(element) == True:
            count += 1
            if element > greatest:
                greatest = element
    my_tuple = (count,greatest)
    return  my_tuple

print("Tuplu: ",create_tuple([111,2002,87,123321,50,9889]),end="\n\n")


'''Problema 8.'''

def divisible_by_x(x,strings,flag=True,default_value=1):
    list_of_lists = []
    if flag == True:
        for string in strings:
             new_list = []
             for i in range(0,len(string)):
                if ord(string[i]) % x == 0:
                   new_list.append(string[i])
             list_of_lists.append(new_list)
    else:
        for string in strings:
             new_list = []
             for i in range(0,len(string)):
                if ord(string[i]) % x != 0:
                   new_list.append(string[i])
             list_of_lists.append(new_list)
    return list_of_lists


print("ASCII code divisible by x: ",divisible_by_x(2,["test","hello", "lab002"],False),end="\n\n")

'''Problema 9. A list of tuples (line, column) each one representing a seat of a spectator which can't see the game '''

def stadium(matrix):
    list_of_tuples = []
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[row])):
            for i in range(row+1,len(matrix)):
                if matrix[row][column] >= matrix[i][column]:
                    list_of_tuples.append((i,column))
    list_of_tuples = list(dict.fromkeys(list_of_tuples))
    return list_of_tuples


print("List of tuples",stadium([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]]),end="\n\n")


'''Problema 10. '''

def pb_10(lists):
    number_of_lists = len(lists)
    maximum = 0
    for i in range(0, number_of_lists):
        if len(lists[i]) > maximum:
            maximum = len(lists[i])
    list_of_tuples = []
    count = 0
    print(len(list_of_tuples))
    i = 0
    for j in range(0, maximum):
        list_of_tuples.append([])
        for i in range(0, number_of_lists):
                if j > len(lists[i]) - 1:
                    list_of_tuples[j].append(None)
                else:
                    list_of_tuples[j].append(lists[i][j])

    return list_of_tuples


print("Problema 10: ",pb_10([[1,2,3], [5,6,7], ["a", "b", "c","d"]]),end="\n\n")

'''Problema 11. '''
