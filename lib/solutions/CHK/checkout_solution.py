

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    costs = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40}
    dict = {}
    for c in skus:
        if c not in costs.keys():
            return -1
        if c in dict:
            dict[c]+=1
        else:
            dict[c] = 1

    # Calculate cost
    total = 0
    print(dict)
    for product in dict.keys():
        if product =='A':
            if dict['A']>=5:
                price = (dict['A'] // 5)*200+(dict['A'] % 5)*costs['A']
            else:
                price = (dict['A'] // 3)*130+(dict['A'] % 3)*costs['A']
        elif product =='B':
            price = (dict['B']// 2)*45+(dict['B'] % 2)*costs['B']
        else:
            # Use unit prices
            price = dict[product] *costs[product]

            # Get one free offer
            if product =='E' and dict['B']>0:
                price -= (dict['E']// 2)*costs['B']  
           
        total += price


    return total


