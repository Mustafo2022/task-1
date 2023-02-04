def is_all(str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char_field in alpha:
        if char_field not in str.lower():
            return False
    return True


stron = input('Enter your Text: ')

if (is_all(stron) == True):
    print("Exists!")
else:
    print("Not Exists!")
