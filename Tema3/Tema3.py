'''Problema 1'''

def lists_to_list_of_sets(list_a,list_b):
    x1 = set(list_a)
    x2 = set(list_b)
    x3 = x1.copy().intersection(x2.copy())
    list_of_sets = []
    list_of_sets.append(x3.copy())
    x4 = x1.copy().union(x2.copy())
    list_of_sets.append(x4)
    x5 = x1.copy().difference(x2.copy())
    list_of_sets.append(x5)
    x6 = x2.copy().difference(x1.copy())
    list_of_sets.append(x6)
    return list_of_sets

print(lists_to_list_of_sets([1,2,3,4,5],[2,3,4,5,6,7]))

'''Problema 2'''

def string_to_dict(string):
    dictionary = {}
    for i in range(0,len(string)):
        if not (string[i] in  dictionary):
            x = string.count(string[i])
            dictionary.setdefault(string[i],x)
    return dictionary

print(string_to_dict("Ana has apples."))

'''Problema 3'''

def compare_2_dictionaries(dict1,dict2):
    for i in dict1.keys():
        if i in dict2:
            if not (dict1.get(i) == dict2.get(i)):
                return False
        else:
            return False
    if len(dict1) == len(dict2):
        return True
    else:
        return False

print(compare_2_dictionaries({"A":1,"B":2},{"A":1,"B":2,}))
print(compare_2_dictionaries({"A":1,"B":2},{"A":1,"C":2,}))
print(compare_2_dictionaries({"A":1,"B":2},{"A":1,"B":2,"D":1}))

'''Problema 4.'''

def  build_xml_element(tag, content, **key_value):
    string = ""
    for i in key_value.keys():
        string = string + str(i) + " = \"" + str(key_value.get(i)) + "\" "
    final_string = "<" + tag + " " + string + "> " + content + " </" + tag + ">"
    print(final_string)

build_xml_element("a","Hello There", href = "http://python.org", _class =" my-link ", id= " someid ")


'''Problema 6'''

def my_tuple(list):
    x = set(list)
    nr_of_unique_elements = len(x)
    nr_of_duplicates = 0
    for element in x:
        if list.count(element) > 1:
            nr_of_duplicates+=1
    return nr_of_unique_elements,nr_of_duplicates

print(my_tuple([1,2,3,4,4,5,6,2,1,20,30]))

'''Problema 7'''

def my_function(*sets):
    dictionary = { }
    for x in sets:
        for y in sets:
            if x!=y:
                dictionary["{} | {}".format(x,y)] = x.union(y)
                dictionary["{} & {}".format(x,y)] = x.intersection(y)
                dictionary["{} - {}".format(x,y)] = x.difference(y)
                dictionary["{} - {}".format(y,x)] = y.difference(x)
    return dictionary

print(my_function({1,2},{2,3}))

'''Problema 9'''


def keywords(*args,**kwargs):
    new_list = list(kwargs.values())
    nr_of_values_found = 0
    for i in args:
        if new_list.count(i)>0:
            nr_of_values_found+=1
    return nr_of_values_found

print(keywords(1, 2, 3, 4, x=1, y=2, z=3, w=5))






