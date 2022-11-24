data = ["1234", "123456","12345678910","1234567","013","011","7543210","12345","1238974"]

firstlist = []
secondlist = []



def tuple_of_item(arg):
    x = 0
    while x < len(arg):
        if len(arg[x]) <= 4:
            firstlist.append(arg[x])
        elif len(arg[x]) >=7:
            secondlist.append(arg[x])
        x = x+1
    x = (firstlist,secondlist)
    print(x)

tuple_of_item(data)




