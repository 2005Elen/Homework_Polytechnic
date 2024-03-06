while True:
    name = input('enter a name of file ')
    try:
        my_file = open(name, 'r')
        print(*my_file)
        my_file.close()
        break

    except FileNotFoundError:
        print('Such file does not exist. Enter the file name again ')
    
    except ValueError:
        print('Non-numeric input. Enter the file name again ')
        
qw = int(input('Do you want to writh to the same file(1) or a new file(2). Enter a number 1 or 2 '))
s = input('Enter text')

while True:
    if qw == 1:
        f = open(name, 'a')
        print(s, file = f)
        f.close()
        break
    elif qw == 2:
        with open('temp.txt', 'w') as f:
            f.write(s)
            f.close()
            break
    else:
        print('Error. Enter a number 1 or 2 ')

