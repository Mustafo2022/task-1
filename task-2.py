a = input('Enter the text: ')
b = input("Enter the substring to search: ")

if a and b:
    lis = a.split()
    if lis:
        if b in lis:
            print('This word exists in your text!')
        else:
            print('This word not exists in your text!')
