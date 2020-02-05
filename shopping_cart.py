# shopping_cart.py

#from pprint import pprint
#from send_email import*

import pandas as pd
import datetime
from decimal import Decimal
from send_email import sendEmail

#load_dotenv()

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

stats = pd.read_csv("/Users/ahmadwilson/OneDrive/PythonProjects/shopping-cart/products.csv")
newDict = stats.to_dict("records")
tester = newDict[1]
identifier = "-1"
#matchingProduct = p for p in newDict if p["id"] = identifier
#newList = []
#matching_products = []
#breakpoint()
#while identifier != "0":
id_list = [str(d["id"]) for d in newDict]
#print (id_list)
product_list=[]
while (True):
    identifier = input("Please input a product identifier. Enter 0 when finished.\t")
    if (identifier == "0"):
        break
    elif identifier not in id_list:
        print("Sorry you entered the wrong ID. Try again")
    else:
        matching_products = [p for p in newDict if str(p["id"]) == str(identifier)]
        #print (matching_products)
        matching_product = matching_products[0]
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
    a = a + "CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M %p" + "\n")
    a = a + "---------------------------------\nSELECTED PRODUCTS:"

    price = 0

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
    tax_price = price* (.085)
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
print (receipt_generator(product_list))
email_choice = input("Would you like to receive a receipt via email?\nEnter y/n\t")

if (email_choice == "y"):
    customer_email = input("Enter your email address:\t")
    sendEmail(customer_email, receipt_generator(product_list))
else:
    print("Have a great day!!!")
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
#> ---------------------------------