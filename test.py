import requests
from decimal import Decimal
from currency import convert


correct = Decimal('3754.8057')
result = convert(Decimal("1000.1000"), 'USD', 'JPY', "14/02/2021", requests)
if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
