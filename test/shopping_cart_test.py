from app.shopping_cart import to_usd, product_finder
from app.send_email import sendEmail


def test_to_usd():
    
    assert to_usd(2.5) == "$2.50"

    assert to_usd(2.50) == "$2.50"

    assert to_usd(2.555556) == "$2.56"

    assert to_usd(1234567890.678) == "$1,234,567,890.68"

    assert to_usd(2.555556) == "$2.56"