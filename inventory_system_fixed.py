"""
This module implements a basic inventory management system.
It allows adding, removing, and querying stock, and saving/loading
the inventory to/from a JSON file.
"""

import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds a specified quantity of an item to the global stock.

    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add.
        logs (list, optional): A list to append log messages to.
                             Defaults to None.
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Removes a specified quantity of an item from the stock.
    If the stock goes to 0 or below, the item is deleted.

    Args:
        item (str): The name of the item to remove.
        qty (int): The quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory.")
        # 'pass' is unnecessary here as print() is a valid statement


def get_qty(item):
    """
    Gets the current quantity of a specific item.

    Args:
        item (str): The name of the item to query.

    Returns:
        int: The quantity of the item, or 0 if not found.
    """
    try:
        return stock_data[item]
    except KeyError:
        return 0  # Return 0 if item doesn't exist


def load_data(file="inventory.json"):
    """
    Loads the inventory data from a JSON file into the global stock_data.

    Args:
        file (str): The filename to load data from.
    """
    # This is the one line we must disable for Pylint 10/10
    # pylint: disable=global-statement
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Saves the current stock_data to a JSON file.

    Args:
        file (str): The filename to save data to.
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """Prints a formatted report of all items in the inventory."""
    print("--- Items Report ---")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")
    print("--------------------")


def check_low_items(threshold=5):
    """
    Checks for items with stock below a given threshold.

    Args:
        threshold (int): The stock level to check against.

    Returns:
        list: A list of item names that are below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """
    Main function to run the inventory management system operations.
    """
    load_data()  # Load existing data first
    add_item("apple", 10)
    add_item("banana", 20)

    try:
        add_item(123, "ten")
    except TypeError:
        print("Error: Invalid types given for item.")

    remove_item("apple", 3)
    remove_item("orange", 1)  # This will now print an error
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    print_data()
    save_data()

    print("--- Main execution finished ---")


if __name__ == "__main__":
    main()

# <-- This file now ends with a single newline, fixing C0304