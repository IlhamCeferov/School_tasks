
class Inventory:
    # Task 1 , 4
    def __init__(self, items = None):
        if items is None:
            self.items = []
        else:
            self.items = items
        # Task 5: initialize the spells dictionary
        self.spells = {}

    # Task 2: print the contents of the items list
    def print_items(self):
        print("Inventory Items:")
        if not self.items:
            print("The inventory is empty.")
        else:
            for item in self.items:
                print(f"- {item}")
        print()

    # Task 3: adding an item to the items list
    def ad_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to the inventory.")

    # Task 5 method to add spell to spell dictionary
    def add_spell(self, spell_name, description):
        self.spell[spell_name] = description
        print(f"Learned spell: '{spell_name}' ")

    # Task 5 method to print spell dictionary
    def print_spells(self):
        print("Known Spells")
        if not self.spells:
            print("No spells learned yet")
        else:
            for name, description in self.spells.items():
                print(f"- {name}: {description}")
        print()

#Testing the main

if __name__ == "__main__":
    print("1.Testing Default Constructor")
    my_inventory = Inventory()
    my_inventory.print_items()

    print("2.Testing adding items")
    my_inventory.add_item("Health potion")
    my_inventory.add_item("Iron sword")
    my_inventory.add_item("Shield")
    print()
    my_inventory.print_items()

    print("3.Testing Constructor with Initial List")
    starting_items = ["Map", "Compass"]
    scout_inventory = Inventory(starting_items)
    scout_inventory.print_items()

    print("4.Testing Spells Dictionary")
    my_inventory.add_spell("healing spell", "this spell heals")
    my_inventory.add_spell("fireball", "deals fire damage to enemies")
    print()
    my_inventory.print_spells()

