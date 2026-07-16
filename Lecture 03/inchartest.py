inchar = input("Input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put Upper Case Letter.")
elif inchar >= 'a' and inchar <= 'z' :
    print("You input a lowercase letter.")
elif inchar >= '0' and inchar <= '9':
    print("You in put Number", inchar)
else :
    print("it'a not a letter or number.", inchar)