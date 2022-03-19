

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus.upper()
    costs = {'A':50, 'B':30, 'C':20, 'D':15}
    dict = {}
    for c in skus:
        if c in dict:
            dict[c]+=1
        else:
            dict[c] = 1

    # Calculate cost
    total = 0
    print(dict)
    for product in dict.keys():
        if product =='A' and dict[product] == 3:
            price = 130
        elif product =='B' and dict[product] == 2:
            price = 45
        else:  # Use unit prices
            price = dict[product] *costs[product]

        total += price


    return total









