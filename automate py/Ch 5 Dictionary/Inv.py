#Fantasy Game Inventory

stuff = {'rope' : 1,
         'torch' : 6,
         'gold chain' : 42,
         'dagger' : 1,
         'arrow' : 12
    }

def displayInv(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('Total number of items: ' + str(item_total))

#displayInv(stuff)

#list to dictionary

def addToInv(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory

inv = {'gold coin': 42,
       'rope': 1}

dragonLoot = ['gold chain', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInv(inv, dragonLoot)
displayInv(inv)
