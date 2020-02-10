# shopping_cart.py

#from pprint import pprint
#from send_email import*

import pandas as pd
import datetime
import os
import csv
from decimal import Decimal
from send_email import *
from spreadsheet import *


load_dotenv()

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


#OLD WAY OF USING os environ files


#fileName = os.environ.get("CSV_FILE_PATH")
#stats = pd.read_csv(fileName)
#newDict = stats.to_dict("records")


newSheet = get_spreadsheet() #custom function that 
PRODUCTS_LIST = newSheet.get_all_records()
newDict = [str(d["id"]) for d in PRODUCTS_LIST]
print (newDict)
#dict = newDict[0]
#print (type(dict))
#breakpoint()
num_rows = len(PRODUCTS_LIST) + 1
print(num_rows)

### THIS while loop allows you to input a new barcode MAY work with barcode scanners
input_qualifier = input("Would you like to add a new product to the directory?\tEnter y/n\t")
if (input_qualifier.lower() == "y"):

    while(True):

        barcode = str(input("Please input barcodes as integers. Input DONE when finished\t"))
        if (barcode.upper() == "DONE"):
            break

        elif barcode.isnumeric() != True or (barcode) in newDict:
            barcode = input("Incorrect input. Please input barcodes as integers. Input DONE when finished\t")

        elif barcode.isnumeric: #and barcode not in [d["id"] for d in newDict]:
            print("Adding ", barcode)
            name = input("Input the product's name\t")
            department = input("Input the product's department\t")
            price = float(input("Input the product's price in the form (0.00) \t"))
            #while price is not float():
            price_per = input("Input how the item is priced. Enter 'pound' or 'item'\t")
            while price_per.lower() != "pound" and price_per.lower()!= "item": 
                price_per = input("Try again. Input how the item is priced. Enter 'pound' or 'item'\t")
            next_row = {
            'id': barcode, 
            'name': name, 
            'department': department, 
            'price': price,
            'availability date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'price_per': price_per
            }
            PRODUCTS_LIST.append(next_row)
            next_row = list(next_row.values())


            num_rows = num_rows + 1
            newSheet.insert_row(next_row, num_rows)
elif input_qualifier.lower() != "n" and input_qualifier.lower()!= "y":
    print("Entered the wrong character. Moving on\n")\


#print(PRODUCTS_LIST)
#breakpoint()


#tester = newDict[1]
#identifier = "-1"
#matchingProduct = p for p in newDict if p["id"] = identifier
#newList = []
#matching_products = []
#breakpoint()
#while identifier != "0":
#id_list = [str(d["id"]) for d in newDict]
#print (id_list)
newDict = [str(d["id"]) for d in PRODUCTS_LIST]
product_list=[]
while (True):
    identifier = input("Please input a product identifier. Enter DONE when finished.\t")
    if (identifier.upper()== "DONE"):
        break
    elif identifier not in newDict:
        print("Sorry you entered the wrong ID. Try again")
    else:
        matching_products = [p for p in PRODUCTS_LIST if str(p["id"]) == str(identifier)]
        #print (matching_products)
        matching_product = matching_products[0]
        if matching_product["price_per"] == "pound":
            num_items = (input("Enter pounds of " + matching_product["name"] + "as an integer or float\t"))
           # while num_items.isnumeric()!= True: #include decimal of this
            matching_product["price"] = matching_product["price"] * float(num_items)
                
                #num_items = (input("Bad Input. Enter number of " + matching_product["name"] + "\t"))
            #for i in range(0,int(num_items)):
            #    print(str(i+1) + " item")
            #    product_list.append(matching_product)
        
        product_list.append(matching_product)

        #print (str(matching_product["id"]) + " "+ str(matching_product["name"])+ " " + str(matching_product["price"])+ " ")


        
        #print("Inside for loop")
        #print
    #newList.append(newDict.)
    
    

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)


def receipt_generator(list):
    now = datetime.datetime.now()
    a = """---------------------------------\n"""
    a= a+ "GEORGETOWN GROCERS\n"
    a = a+ "WWW.GEORGETOWN-GROCERS.COM\n---------------------------------\n"
    receipt_time = now.strftime("%Y-%m-%d %I:%M %p" + "\n")
    a = a + "CHECKOUT AT: " + receipt_time
    a = a + "---------------------------------\nSELECTED PRODUCTS:"

    price = 0
    price = float(price)

    for p in product_list:
        a= a+("\n... " + p["name"] + " (" + to_usd(p["price"]) +")")
        price = price + p["price"]
    
    a= a+"\n---------------------------------\nSUBTOTAL: "
    a= a+ to_usd(price)

    """
    print("---------------------------------")
    print("SUBTOTAL: " + to_usd(price))
    """
    #tax_price = Decimal
    #load_dotenv()
    tax_rate= " "
    tax_rate = os.environ.get("CUSTOM_TAX")
    #tax
    #tax_rate = str(tax_rate)
    #breakpoint()
    #breakpoint()
    tax_rate = float(tax_rate)
    
    tax_price = price* (tax_rate)
    #tax_price = to_usd(tax_price)
    a = a + "\nTAX: " + to_usd(tax_price)

    """
    print("TAX: " + to_usd(tax_price))
    """

    a = a + "\nTOTAL: " + to_usd(price+tax_price)
    a = a + "\n---------------------------------"
    a = a + "\nTHANKS, SEE YOU AGAIN SOON"
    a = a + "\n---------------------------------"

    """
    print("TOTAL: " + to_usd(price+tax_price))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON")
    print("---------------------------------")
    
    #now = datetime.datetime.strftime("%Y, %m", "%d", "%I", "%M", "%p")


    print("---------------------------------")
    print("GEORGETOWN GROCERS")
    print("WWW.GEORGETOWN-GROCERS.COM")
    print("---------------------------------")
    print("CHECKOUT AT: ", now.strftime("%Y-%m-%d %I:%M %p"))
    print("---------------------------------")
    print("SELECTED PRODUCTS:")
    """
    """
    price = 0
    #price = Decimal(price)
    #price = to_usd(price)
    
    for p in product_list:
        print("... " + p["name"] + " (" + to_usd(p["price"]) +")")
        price = price + p["price"]
    
    tax_price = price* (.085)
    #price = to_usd(price)
    #price = round(price,2)
    print("---------------------------------")
    print("SUBTOTAL: " + to_usd(price))
    #tax_price = Decimal
    

    #tax_price = to_usd(tax_price)
    print("TAX: " + to_usd(tax_price))
    print("TOTAL: " + to_usd(price+tax_price))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON")
    print("---------------------------------")
    """
    return a
    

#receipt_generator(product_list)
#print ("STARTING A ")
receipt_time = ""
now = datetime.datetime.now()
receipt_time = now.strftime("%Y-%m-%d-%H-%M-%S-%f")



final_receipt = receipt_generator(product_list)
print (final_receipt)
email_choice = input("Would you like to receive a receipt via email?\tEnter y/n\t")

if (email_choice.lower() == "y"):
    customer_email = input("Enter your email address:\t")
    sendEmail(customer_email, receipt_generator(product_list))
else:
    print("\n")

print_choice = input("Would you like a physical copy of the receipt?\tEnter y/n\t")
#print(file_name)
if print_choice.lower() == "y":
    file_name = os.path.join(os.path.dirname(__file__), "receipts", receipt_time + ".txt") # a relative filepath
    #print(file_name)
    #breakpoint()
    with open(file_name, "w") as file: # "w" means "open the file for writing"
       file.write(final_receipt)
       print("Receipt generated in receipts folder")
    
print("Have a good day\n")


#print("---------------------------------")
#print("Generating receipt to email")
#print("---------------------------------")
#sendEmail("asw99@georgetown.edu", receipt_generator(product_list))
# TODO: write some Python code here to produce the desired output

#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2019-06-06 11:31 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "sheets-test-267401-1f8951c41319.json")