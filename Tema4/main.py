import os

'''Problema 1. Enumarare extensii fisiere director dat'''


def listing(path):
    list_of_files = os.listdir(path)
    set_of_extensions = list()
    for file in list_of_files:
        x = file.split(".", 1)
        try:
            set_of_extensions.append(x[1])
        except Exception as e:
            continue
    new_set = set(set_of_extensions)
    new_set = sorted(new_set)
    print(new_set)


listing(".")

'''Problema 2. '''


def dir_and_file(dir_path, file_path):
    fd = open(file_path, 'w')
    list_of_files = os.listdir(dir_path)
    for file in list_of_files:
        fd.write("{}\n".format(os.path.join(dir_path, file)))
    fd.close()


dir_and_file("/Users/lilschnapsidee/Desktop/ML", "/Users/lilschnapsidee/Desktop/file.txt")

'''Problema 3.'''


def dir_or_file(my_path):
    if os.path.isfile(my_path):
        fd = open(my_path, 'r')
        data = fd.read()
        i = -20
        last_characters = ""
        while i < 0:
            last_characters += data[i]
            i += 1
        return last_characters
    list_of_extensions = []
    if os.path.isdir(my_path):
        for (root, directories, files) in os.walk(my_path):
            for fileName in files:
                split_tup = os.path.splitext(fileName)
                list_of_extensions.append(split_tup[1])
    list_of_tuples = []
    for ext in list_of_extensions:
        list_of_tuples.append((ext, list_of_extensions.count(ext)))
    list_of_tuples = set(list_of_tuples)
    print(list_of_tuples)


dir_or_file("/Users/lilschnapsidee/Desktop/file.txt")
dir_or_file("/Users/lilschnapsidee/Desktop/ML")

'''Problema 4.'''


def command_line():
    path = input("Path: ")
    if os.path.isdir(path) == False:
        return 0
    list_of_files = os.listdir(path)
    list_of_extensions = []
    for file in list_of_files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            split_tup = os.path.splitext(file)
            list_of_extensions.append(split_tup[1])
    final_list = []
    for ext in list_of_extensions:
        if list_of_extensions.count(ext) == 1:
            final_list.append(ext)
    return final_list


print(command_line())

'''Problema 5.'''


def my_function(target, to_search):
    lista_de_fisiere = []
    if os.path.isfile(target):
        fd = open(target, 'r')
        data = fd.read()
        if data.find(to_search):
            lista_de_fisiere.append(os.path.basename(target))
        fd.close()
        return lista_de_fisiere
    if os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for fileName in files:
                pathname = os.path.join(target, fileName)
                fd = open(pathname, 'r')
                data = fd.read()
                if data.find(to_search):
                    lista_de_fisiere.append(os.path.basename(fileName))
                fd.close()
        return lista_de_fisiere
    else:
        raise ValueError("Target nu este nici fisier, nici director :/")



print(my_function("/Users/lilschnapsidee/Desktop/untitled folder", "lilschnapsidee"))

'''Problema 7.'''

def dictionar(path):
    dictionar_fisier = {}
    dictionar_fisier.setdefault("full_path",path)
    dictionar_fisier.setdefault("file_size",os.path.getsize(path))
    file_ext = os.path.splitext(path)
    dictionar_fisier.setdefault("file_extension",file_ext[1])
    bool_can_write = os.access(path,os.W_OK)
    dictionar_fisier.setdefault("can_write",bool_can_write)
    bool_can_read = os.access(path, os.R_OK)
    dictionar_fisier.setdefault("can_read",bool_can_read)
    print(dictionar_fisier)

dictionar("/Users/lilschnapsidee/Desktop/lab5_CSSO.txt")

'''Problema 8.'''

def absolute_path(dir_path):
    list_of_paths = []
    list_of_files = os.listdir(dir_path)
    for file in list_of_files:
        abs_path = os.path.abspath(os.path.join(dir_path, file))
        if os.path.isfile(abs_path):
            list_of_paths.append(abs_path)
    return list_of_paths


print(absolute_path("/Users/lilschnapsidee/Downloads"))



