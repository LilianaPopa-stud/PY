import os
import re
import xml.etree.ElementTree as ET

#Ex. 1
def extract_words(text):
    words = []
    for word in text.split():
        if word.isalnum():
            words.append(word)
    return words

#Ex. 2

def substrings(regex, text, x):
    words = []
    for word in text.split():
        if len(word) == x and re.match(regex, word):
            words.append(word)
    return words

#Ex. 3

def regular_expression(text, regular_expressions):
    matches = []
    for regex in regular_expressions:
        matches += re.findall(regex, text)
    return matches

#Ex. 4
def xml_elements(path, attributes):
    tree = ET.parse(path)
    root = tree.getroot()
    result = []
    for child in root:
        ok = True
        for key in attributes:
            if child.attrib[key] != attributes[key]:
                ok = False
        if ok:
            result.append(child)
    return result

#Ex. 5
def xml_elements2(path, attributes):
    tree = ET.parse(path)
    root = tree.getroot()
    result = []
    for child in root:
        ok = True
        for key in attributes:
            if child.attrib[key] != attributes[key]:
                ok = False
        if ok:
            result.append(child)
    return result

#Ex. 6
def censure(text):
    all_matches = re.findall('[aeiouAEIOU]\w*[aeiouAEIOU]', text)
    censured_matches = []
    for match in all_matches:
        tmp = ''
        for i in range(1, len(match) + 1):
            if i % 2 == 0:
                tmp += match[i - 1]
            else:
                tmp += '*'
        censured_matches.append(tmp)
    return censured_matches

#Ex. 7
def is_cnp(cnp):
    if re.match("^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",cnp):
        return True
    return False

print(is_cnp("8000614225823"))

#Ex. 8
def list_files(path,regex):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path + "/" + file):
            if re.match(regex, file):
                print(">>" + file)
            elif re.search(regex, file):
                print(file)
