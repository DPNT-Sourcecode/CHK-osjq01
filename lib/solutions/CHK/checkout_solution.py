

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    costs = {'A':50, 
    'B':30, 
    'C':20, 
    'D':15, 
    'E':40, 
    'F':10, 
    'G':20, 
    'H':10, 
    'I':35, 
    'J':60, 
    'K':80, 
    'L':90, 
    'M':15, 
    'N':40, 
    'O':10, 
    'P':50, 
    'Q':30, 
    'R':50, 
    'S':30, 
    'T':20,
    'U':40, 
    'V':50, 
    'W':20,
    'X':90,
    'Y':10, 
    'Z':50}

    initial_discounts={'A':

    }
    dict = {}
    for c in skus:
        if c not in costs.keys():
            return -1
        if c in dict:
            dict[c]+=1
        else:
            dict[c] = 1

    # First remove those free items
    if 'E' in dict:
        freeB = dict['E']//2
        if 'B' in dict:
            if dict['B']>freeB:
                dict['B']-=freeB
            else:
                dict.pop('B')

    if 'F' in dict and dict['F'] >=3:
        dict['F'] -= dict['F']//3
        
    # Calculate cost
    total = 0
    for product in dict.keys():
        if product =='A':
            price = (dict['A'] // 5)*200
            left_unit = dict['A']%5
            price += (left_unit // 3)*130+(left_unit % 3)*costs['A']
        elif product =='B':
            price = (dict['B']// 2)*45+(dict['B'] % 2)*costs['B']
        if product =='H':
            price = (dict['H'] // 10)*80
            left_unit = dict['H']%10
            price += (left_unit // 5)*45+(left_unit % 3)*costs['H']
       
        else:
            # Use unit prices
            price = dict[product] *costs[product]
           
        total += price


    return total


