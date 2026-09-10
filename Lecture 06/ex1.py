heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

def display_heroes(heroes):
    for hero in heroes:
        print(heroes)
        
def add_heroes(heroes, hero):
    for hero in heroes:
        heroes.append(hero)
        
def insert_heroes(heroes, index, hero):
    heroes.insert(index, hero)
    
def remove_heroes(heroes, hero):
    heroes.remove(hero)

# add_heroes(heroes, 'Batman')
display_heroes(heroes)