animals = ['cat','dog','rabbit','hamster','dog','parrot']
first_dog_index = animals.index("dog")
print(f'The first of dog: {first_dog_index}')

second_dog_index = animals.index("dog", first_dog_index + 1)
print(f'the second of dog: {second_dog_index}')