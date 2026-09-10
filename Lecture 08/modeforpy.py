def example_w_plus_mode():
    with open('example_w+.txt', 'w+') as file:
        file.wrote("this is the first line in ther file. \n")
        file.wrote("this is the second line in ther file. \n")
        
        file.seek(0)
        
        content = file.read()
        print("Content of the file:")
        print(content)
        
example_w_plus_mode