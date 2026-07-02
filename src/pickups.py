
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]



# Player inventory
inventory = []

def get_item_score(item):
    '''
    Check if item os a frute or not - if a frute increase value on item
    add item in a list
    '''
    #print("get_item_score")
    pickup_item(item)
    if item.name != "meatball":
        item.value = 20

def pickup_item(item):
    """Add an item to the player's inventory."""
    if item is not None:
        inventory.append(item)

def pickup_print_list():
    return inventory
    '''
    print("Inventory")
    print("--------------------------------------")
    if len(inventory) > 0:
        for item in inventory:
            print("| " + item.name)
        print("--------------------------------------")
    else:        
        print("youre inventory i empty: 0")
    '''

def pickup_print_list2():
    # print out whtout curser modeul
    print("Inventory")
    print("--------------------------------------")
    if len(inventory) > 0:
        for item in inventory:
            print("| " + item.name)
        print("--------------------------------------")
    else:        
        print("youre inventory i empty: 0")
    
def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

