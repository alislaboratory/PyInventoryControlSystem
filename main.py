import csv
import os # Import needed libraries.
import time

# Create empty lists to store products and fields.
products = []
fields = []
filename = "inventory.csv"
# Store filename of the CSV file

class Item: # Here, we create a class 'Item' to store the information for a particular product. This essentially gives us a custom datatype to work with

    # Assigning member variables their values
    def __init__(self, partNo, partName, make, model, quantity, price):
        self.partNo = partNo
        self.partName = partName
        self.make = make
        self.model = model
        self.quantity = quantity
        self.price = price

# This function converts the CSV into a list of 'Item' objects.
# It is better to store them in memory because it is faster and constant reading and writing may corrupt the file in a complete loss of data.
def csv_to_list():
    with open(filename, 'r') as f: # Open the file
        csvreader = csv.reader(f)
        fields = next(csvreader) # Handle CSV

        for row in csvreader: # Make each row an 'Item object'
            print(row)
            item = Item(row[0], row[1], row[2], row[3], row[4], row[5])
            products.append(item) # Append it to the list of objects
csv_to_list()

# This function converts our list of 'Item' objects to a new CSV file. It creates a new one because CSV files cannot be overwritten, and
# it is risky as it can result in file corruption and data loss.
def products_to_csv(products):
    os.remove(filename)
    with open(filename, 'w') as f: # Open the file
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields) # Handle CSV

        for product in products: # Write the 'Item' object's properties to a CSV row for each product
            csvwriter.writerow([product.partNo, product.partName, product.make, product.model, product.quantity, product.price])




# A very simple function to find the average item price
def average_item_price(products):
    sum = 0
    count = 0

    for product in products:
        count += 1
        sum += float(product.price) * int(product.quantity) # Add the product price * its respective quantity (frequency)

    return sum/count # Return the average (mean)

# Same as the avg item price function, but returns the sum as well for the statistics function.
def basic_stats(products):
    sum = 0
    count = 0

    for product in products:
        count += 1
        sum += float(product.price)

    return sum / count, sum

# Function to add an item to the list of products
def add_item():
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    partNo = input("Enter partNo: ") # Ask for user input
    partName = input("Enter part name: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")

    new_item = Item(partNo, partName, make, model, quantity, price) # Create an Item object
    products.append(new_item) # Append object to list of products

# Function to update the item. Uses partNo to find the product
def update_item():
    partNo = input("Enter the partNo: ") # User input
    for product in products:
        if product.partNo == partNo:
            index = products.index(product) # Find the index of the product in the list based on the part number by using inbuilt function .index()

    item = products[index]
    quantity = input("Enter the new quantity: ")
    item.quantity = int(quantity)

# Function to delete the item. Uses partNo to find the product
def delete_item():
    partNo = input("Enter the partNo: ") # User input
    for product in products:
        if product.partNo == partNo:
            index = products.index(product)

    products.pop(index) # .pop() removes an element from a list with an index


# Simple function to display items with print
def display_items():
    print("PartNo, PartName, Make, Model, Quantity, Price") # Fields
    for product in products:
        print(f"{product.partNo}, {product.partName}, {product.make}, {product.model}, {product.quantity}, {product.price}")

# Function to return a list of products that have a quantity less than 4
def quantity_greaterthan_4(products):
    newList = products # Create a copy of products
    for product in newList:
        if int(product.quantity) >= 4:
            newList.pop(newList.index(product))

    return newList

# Function to return a list of products that have a price greater than X value
def price_greaterthan_select(products):
    value = input("Greater than what price? ") # User input
    newList = products
    for product in newList:
        if float(product.price) <= float(value):
                newList.pop(newList.index(product))

    return newList

# Function to return a list of products that have a price greater than the average of all product prices
def greater_than_avg(products):
    newList = products
    avgprice = average_item_price(newList) # Use a function I made above to find the average
    print(avgprice)

    for product in newList:
        if float(product.price) <= float(avgprice):
            newList.pop(newList.index(product))
    return newList

# Function to return basic stock statistics
def stock_statistics():
    print(f"Stock evaluation: {basic_stats(products)[1]}")
    print(f"Average price: {basic_stats(products)[0]}")



# Main loop
if __name__ == "__main__": # Only run the main loop if this file is being run directly, not accessed from another file
    while True:
        # Print selections to screen
        print("")
        print("")
        print("Inventory Control System")
        print("[1] Add Item")
        print("[2] Update Item")
        print("[3] Delete Item")
        print("[4] Display Inventory")
        print("[5] Display Re-ordered List")
        print("[6] Display parts greater than selected price")
        print("[7] Display parts greater than the average price")
        print("[8] Inventory statistics summary")
        print("")
        print("[9] Exit")

        selection = input("Enter your choice: ") # User input
        print("\n\n\n")

        # Simple selection logic. Keeps the main loop clean and readable and leaves the actual logic to the functions.
        if selection == "1": # Use IF statements to find the selection from the input()
            print("Stock Control - Add Item")
            print("========")
            add_item() # Run the function to add items.
            time.sleep(1) # In all of the selection processes, I used a 1 second delay so the user had time to read the output from the function
            # before it continued back to the function selections because of the while loop.

        elif selection == "2":
            print("Stock Control - Update Item")
            print("========")
            update_item()
            time.sleep(1)

        elif selection == "3":
            print("Stock Control - Delete Item")
            print("========")
            delete_item()
            time.sleep(1)

        elif selection == "4":
            print("Display - All Inventory")
            print("========")
            display_items()
            time.sleep(1)

        elif selection == "5":
            print("Display - Re-ordered List")
            print("========")
            edited_products = quantity_greaterthan_4(products)

            for product in edited_products: # Here, I loop through the products, and then unwrap the properties and print them to screen.
                print(f"{product.partNo}, {product.partName}, {product.make}, {product.model}, {product.quantity}, {product.price}")
            time.sleep(1)

        elif selection == "6":
            print("Display - Price greater than selected value")
            print("========")
            edited_products = price_greaterthan_select(products)

            for product in edited_products:
                print(f"{product.partNo}, {product.partName}, {product.make}, {product.model}, {product.quantity}, {product.price}")
            time.sleep(1)

        elif selection == "7":
            print("Display - Price greater than average price")
            print("========")
            edited_products = greater_than_avg(products)

            for product in edited_products:
                print(f"{product.partNo}, {product.partName}, {product.make}, {product.model}, {product.quantity}, {product.price}")
            time.sleep(1)
        elif selection == "8":
            print("Display - Stock statistics")
            print("========")
            stock_statistics()
            time.sleep(1)

        elif selection == "9":
            print("Saving records...")
            products_to_csv(products) # Convert our products list in memory back to a CSV file with a function made above.
            print("Exiting...")
            time.sleep(1)
            print("Thank you")
            exit() # This inbuilt Python function returns exit code 0 and quits the program.
        else: # If the selection is not 1-9, tell the user that their input is unknown and restart the loop.
            print("Unknown command. Please select option 1-9.")
            time.sleep(1)


# Elaboration of code

# I used an Item class because I believed it would make it easier to keep track of and handle the items and their properties later on in the more
# complex logic. Evidently, it made the code short and readable, and keeps piecewise complexity and memory usage to a minimum compared to using other datatypes
# which scatter memory allocations all over the place.

# I only used the products list parameter for functions that needed to return something. I did this so those functions that return something (usually a list)
# could be defined outside of the scope of the 'products' list, but called inside of it. Although it wouldn't really affect it anyway, I thought
# it was necessary for redundancy.

# I kept the products in memory until the program exits, when it writes to a CSV. This way, we can avoid file corruption by continuous reading/writing,
# and it would also be faster because the memory is much faster than SDD and hard drive where the CSV file is most likely stored.