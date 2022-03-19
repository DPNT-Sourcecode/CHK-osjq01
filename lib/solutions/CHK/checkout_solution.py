

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
            price = (dict[product] // 3)*130+(dict[product] % 3)*costs[product]
        elif product =='B':
            price = (dict[product]// 2)*45+(dict[product] % 2)*costs[product]
        elif product =='E' and if dict['B']:
                price -= (dict[product]// 2)*costs['B']
        else:  # Use unit prices
            price = dict[product] *costs[product]

        total += price


    return total



