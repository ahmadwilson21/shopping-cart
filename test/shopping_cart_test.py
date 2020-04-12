<<<<<<< HEAD
from app.shopping_cart import to_usd, product_finder, human_friendly_timestamp
import datetime
import pytest
=======
from app.shopping_cart import to_usd, product_finder
from app.send_email import sendEmail
>>>>>>> master


def test_to_usd():
    
    assert to_usd(2.5) == "$2.50"

    assert to_usd(2.50) == "$2.50"

    assert to_usd(2.555556) == "$2.56"

    assert to_usd(1234567890.678) == "$1,234,567,890.68"

<<<<<<< HEAD
    assert to_usd(2.555556) == "$2.56"


def test_human_friendly_timestamp():
    
    assert human_friendly_timestamp(datetime.datetime(year=2020, month =1, day =1, hour = 0, minute= 0))== "2020-01-01 12:00 AM"

def test_product_finder():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    matching_product_one = product_finder(1,products)
    matching_product_two = product_finder(2,products)
    matching_product_three = product_finder(3,products)

    
    assert matching_product_one["name"] == "Chocolate Sandwich Cookies"
    assert matching_product_two["price"] == 4.99
    assert matching_product_three["id"] == 3
    
=======
    assert to_usd(2.555556) == "$2.56"
>>>>>>> master
