stuff = {'arrow' : 12, 'rope' : 1, 'gold coin' : 42,
             'torch' : 6, 'dagger' : 1}

def display(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + "  " + k)
        
    print("Total number of items is: " + str(item_total))

display(stuff)
