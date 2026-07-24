str_input = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in str_input:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_string