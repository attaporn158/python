global_variable = "I'm outside the funtion"

def my_function():
    print(global_variable)
    
my_function()

print(global_variable)