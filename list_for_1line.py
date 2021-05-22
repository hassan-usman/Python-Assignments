fruits = ["mango","strwberry","kiwi","pineapple","apple"]
thislist_10 = [x for x in fruits if"a" in x]
print(thislist_10)
thislist_10 = [x for x in fruits if x != "watermelon"]
print(thislist_10)
thislist_10 = [x for x in fruits]
print(thislist_10)
thislist_10 = [x.upper() for x in fruits]
print(thislist_10)
thislist_10 = ["hello" for x in fruits]
print(thislist_10)
thislist_10 = [x if x != "banana" else"orange" for x in fruits]
print(thislist_10)


