fruits_with_deplicates = ['apple','banana','apple','cherry','apple','kiwi']
while 'apple' in fruits_with_deplicates:
    fruits_with_deplicates.remove('apple')
print(f'Fruits atfer remove: {fruits_with_deplicates}')