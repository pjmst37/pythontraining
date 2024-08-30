try:
    with open('sad.txt', mode='w') as my_file:
        text = my_file.write('hey it\'s me again!')
        print(text)
        # print(my_file.readlines())
except FileNotFoundError as err:
    print("File does not exist")
    raise err
except IOError as err:
    print('IO error')
    raise err
