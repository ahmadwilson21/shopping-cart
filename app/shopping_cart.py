# shopping_cart.py

from dotenv import load_dotenv
import datetime
import os
import csv
from decimal import Decimal



load_dotenv()

def human_friendly_timestamp(my_time):
    """
    Converts datetime object into a readable format
    Params: my_time (datetime.datetime object)

    Example: 
    human_friendly_timestamp(datetime.datetime(
        year=2020, 
        month = 1, 
        day =1, 
        hour = 0, 
        minute = 0))
    
    Returns:
    "2020-01-01 12:00 AM"

    """
    return my_time.strftime("%Y-%m-%d %I:%M %p")

def product_finder(product_id, list):
    """
    Finds an item in a list given its id 
    Params: product_id (int), list (list)
    Example: product_finder(2, [{id: 2, name: "Product 1"}])
    Returns: {id: 2, name: "Product 1"}
    """
    product_list = [p for p in list if str(p["id"]) == str(product_id)]
    return product_list[0]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def receipt_generator(list):
    """
    Converts a list of dictionary items with a 'name' and 'price' identifier into
    a formatted receipt with calculated totals with tax and returns the text as a string.

    Params: 
        list (list)

    Example: 
        receipt_generator([
                            {'id': 1, 
                             'name': 'Product A',
                             'department': 'snacks', 
                             'price': 4.99, 
                             'availability_date': '2019-01-01', 
                             'price_per': 'item'
                             }])
    
    Returns:
        "---------------------------------
        GEORGETOWN GROCERS
        WWW.GEORGETOWN-GROCERS.COM
        ---------------------------------
        CHECKOUT AT: 2020-04-11 06:54 PM
        ---------------------------------
        SELECTED PRODUCTS:
        ... Product A ($4.99)
        ---------------------------------
        SUBTOTAL: $4.99
        TAX: $4.24
        TOTAL: $9.23
        ---------------------------------
        THANKS, SEE YOU AGAIN SOON
        ---------------------------------"
        """

    now = datetime.datetime.now()
    receipt = """---------------------------------\n"""
    receipt = receipt + "GEORGETOWN GROCERS\n"
    receipt = receipt + "WWW.GEORGETOWN-GROCERS.COM\n---------------------------------\n"
    receipt_time = human_friendly_timestamp(now)
    receipt = receipt + "CHECKOUT AT: " + receipt_time + "\n"
    receipt = receipt + "---------------------------------\nSELECTED PRODUCTS:"

    price = 0
    price = float(price)

    for p in list:
        receipt = receipt + ("\n... " + p["name"] + " (" + to_usd(p["price"]) +")")
        price = price + p["price"]
    
    receipt = receipt +"\n---------------------------------\nSUBTOTAL: "
    receipt = receipt + to_usd(price)


    tax_rate= " "
    tax_rate = os.environ.get("CUSTOM_TAX") #user entered Tax Rate
    tax_rate = float(tax_rate)   
    tax_price = price* (tax_rate)
 
    receipt = receipt + "\nTAX: " + to_usd(tax_price)
    receipt = receipt + "\nTOTAL: " + to_usd(price+tax_price)
    receipt = receipt + "\n---------------------------------"
    receipt = receipt + "\nTHANKS, SEE YOU AGAIN SOON"
    receipt = receipt + "\n---------------------------------"

    return receipt


if __name__ == "__main__":
    from send_email import sendEmail
    from spreadsheet import get_spreadsheet

    print("\nWelcome to the Georgetown Grocer Receipt Generator")
    newSheet = get_spreadsheet() #> <class spreadsheet.py> 
    PRODUCTS_LIST = newSheet.get_all_records() ##> <class gspread> generates a list from the googlesheet 
    newDict = [str(d["id"]) for d in PRODUCTS_LIST] #This places all the ids into a list so we can easily determine if an item is in the list
    num_rows = len(PRODUCTS_LIST) + 1 #Adds an extra row to account for the headings

 


    ### THIS code allows you to manually input a new barcode and the information for a new product
    input_qualifier = input("Would you like to add a new product to the spreadsheet database?\tEnter y/n\t")
    if (input_qualifier.lower() == "y"):

        while(True):
            barcode = str(input("Please input barcodes as integers. Input DONE when finished\t"))
            if (barcode.upper() == "DONE"):
                break
            elif barcode.isnumeric() != True or barcode in newDict: # if barcode not a number or is already a created product
                barcode = input("Incorrect input. Please input barcodes as integers. Input DONE when finished\t")
            elif barcode.isnumeric: #if its a number then it will add the barcode
                print("Adding ", barcode)
                name = input("Input the product's name\t")
                department = input("Input the product's department\t")
                price = float(input("Input the product's price as a decimal in the form (0.00) \t"))
                price_per = input("Input how the item is priced. Enter 'pound' or 'item'\t")

                while price_per.lower() != "pound" and price_per.lower()!= "item": 
                    price_per = input("Try again. Input how the item is priced. Enter 'pound' or 'item'\t")

                #nextrow creates an entire new row with the new attributes entered by the user
                # adapted from https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md
                next_row = {
                'id': barcode, 
                'name': name, 
                'department': department, 
                'price': price,
                'availability date': datetime.datetime.now().strftime("%Y-%m-%d"),
                'price_per': price_per
                }
                PRODUCTS_LIST.append(next_row) #adds the new row to product list
                next_row = list(next_row.values()) #collects values in order to add to the google sheet
                num_rows = num_rows + 1 #the new location of the object is the last row position + 1
                newSheet.insert_row(next_row, num_rows) #inserts new row into sheet




    #if you enter the wrong character we just move on
    elif input_qualifier.lower() != "n" and input_qualifier.lower()!= "y": 
        print("Entered the wrong character. Moving on\n")\



    newDict = [str(d["id"]) for d in PRODUCTS_LIST] #This updates newDict with the new values added to the sheet
    scanned_list=[] #this list will hold the items scanned by the cashier




    #This loop has the cashier input all the products that the customer will buy and breaks after entering "done"
    while (True):
        identifier = input("Please input a product identifier. Enter DONE when finished.\t")
        if (identifier.upper()== "DONE"):
            break
        elif identifier not in newDict:
            print("Sorry you entered the wrong ID. Try again")
        else:
            matching_product = product_finder(identifier, PRODUCTS_LIST)
            #matching_product = matching_products[0]
            if matching_product["price_per"] == "pound":
                num_items = (input("Enter pounds of " + matching_product["name"] + "as an integer or decimal\t"))
                matching_product["price"] = matching_product["price"] * float(num_items) #alters the price of said item to reflect price in pounds


            scanned_list.append(matching_product)




    #Generates the receipt time in order to be used as the filename to be printed in a txt file

    receipt_time = ""
    now = datetime.datetime.now()
    receipt_time = now.strftime("%Y-%m-%d-%H-%M-%S-%f")


    #Generates and prints final receipt
    final_receipt = receipt_generator(scanned_list) #> <class shopping_cart.py> 
    print (final_receipt)


    #Enter an email address to send the receipt
    email_choice = input("Would you like to receive a receipt via email?\tEnter y/n\t")
    if (email_choice.lower() == "y"):
        customer_email = input("Enter your email address:\t")
        sendEmail(customer_email, receipt_generator(scanned_list)) #> <class send_email.py> 
    else:
        print("\n")


    #Prints a physical copy of the receipt with the time the receipt was created as the title
    print_choice = input("Would you like a physical copy of the receipt?\tEnter y/n\t")
    if print_choice.lower() == "y":
        file_name = os.path.join(os.path.dirname(__file__), "receipts", receipt_time + ".txt") # a relative filepath
        with open(file_name, "w") as file: # "w" means "open the file for writing"
           file.write(final_receipt)
           print("Receipt generated in receipts folder")
    print("\nHave a good day\n")