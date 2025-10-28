import json
# <-- FIX: Removed unused 'import logging'
from datetime import datetime

# Global variable
stock_data = {}

# <-- FIX: Changed 'addItem' to 'add_item' for snake_case naming
# <-- FIX: Changed 'logs=[]' to 'logs=None' to prevent mutable default argument bug
def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []  # Initialize a new list inside the function
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # <-- FIX: Used an f-string for cleaner formatting
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")

# <-- FIX: Changed 'removeItem' to 'remove_item' for snake_case naming
def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # <-- FIX: Replaced bare 'except:' with 'except KeyError:'
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory.")
        pass # Now safely ignoring only the expected error

# <-- FIX: Changed 'getQty' to 'get_qty' for snake_case naming
def get_qty(item):
    try:
        return stock_data[item]
    except KeyError:
        return 0 # Return 0 if item doesn't exist

# <-- FIX: Changed 'loadData' to 'load_data' for snake_case naming
def load_data(file="inventory.json"):
    # <-- FIX: Used 'with open' to properly manage file resources
    try:
        with open(file, "r", encoding="utf-8") as f: # Added encoding
            global stock_data
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}

# <-- FIX: Changed 'saveData' to 'save_data' for snake_case naming
def save_data(file="inventory.json"):
    # <-- FIX: Used 'with open' to properly manage file resources
    with open(file, "w", encoding="utf-8") as f: # Added encoding
        f.write(json.dumps(stock_data, indent=4)) # Added indent=4 for readability

# <-- FIX: Changed 'printData' to 'print_data' for snake_case naming
def print_data():
    print("--- Items Report ---")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")
    print("--------------------")

# <-- FIX: Changed 'checkLowItems' to 'check_low_items' for snake_case naming
def check_low_items(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    load_data() # Load existing data first
    add_item("apple", 10)
    add_item("banana", 20)
    
    # Example of invalid type, now safely handled in get_qty
    try:
        add_item(123, "ten")  
    except TypeError:
        print("Error: Invalid types given for item.")

    remove_item("apple", 3)
    remove_item("orange", 1) # This will now print an error
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    
    print_data()
    save_data()
    
    # <-- FIX: Removed the dangerous 'eval(...)' line
    print("--- Main execution finished ---")

# Standard check to run main() only when script is executed directly
if __name__ == "__main__":
    main()