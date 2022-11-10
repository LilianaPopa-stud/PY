import utils

def main():
    flag = True
    while flag == True:
        x = input("Enter a number: ")
        if x == "q":
            flag = False
        else:
            x = int(x)
            print(utils.process_item(x))
