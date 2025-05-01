from storage import books
b = books()
while (True):
    v = input ("Would you like to add a book? (Yes, No)")
    if v == "yes":
        c = b.add()
    elif v == "no":
        break
q = input ("Would you like to sell a book? (Yes, No)")
if q == "yes":
    x = b.sell()
g = input ("Would you like to see the books you have?")
if g == "yes":
    h = b.showbook()