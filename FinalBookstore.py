from storage import books
b = books()
v = input ("Would you like to add a book? (Yes, No)")
if v == "yes":
    c = b.add()
q = input ("Would you like to sell a book? (Yes, No)")
if q == "yes":
    x = b.sell()