from storage import books
b = books()
while (True):
    v = input ("1.Add a book \n2.Sell a book \n3.See books I have \n4.Save my books \n5.Open an existing file\n9.Qiut\n")
    if v == "1":
        c = b.add()
    elif v == "2":
        x = b.sell()
    elif v == "3":
        h = b.showbook()
    elif v == "4":
        m = b.savebook()
    elif v == "5":
        o = b.loadbook()
    elif v == "9":
        break
