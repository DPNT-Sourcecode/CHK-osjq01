

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    costs = {
    'A':50, 
    'B':30, 
    'C':20, 
    'D':15, 
    'E':40, 
    'F':10, 
    'G':20, 
    'H':10, 
    'I':35, 
    'J':60, 
    'K':70, 
    'L':90, 
    'M':15, 
    'N':40, 
    'O':10, 
    'P':50, 
    'Q':30, 
    'R':50, 
    'S':20, 
    'T':20,
    'U':40, 
    'V':50, 
    'W':20,
    'X':17,
    'Y':20, 
    'Z':21}

    discounted = {
        'A':[(5, 200), (3, 130)],
        'B':[(2, 45)],
        'H':[(10, 80), (5, 45)],
        'K':[(2, 120)],
        'P':[(5, 200)],
        'Q':[(3, 80)],
        'V':[(3, 130), (2, 90)],
    }

    frees = {
        'E':(2, 'B'),
        'F':(3, 'F'), 
        'N':(3, 'M'),
        'R':(3, 'Q'),
        'U':(4, 'U'),
    }

    anythree = ['Z', 'Y', 'S', 'T', 'X'] # Order from expensive to cheapest

    basket = {}
    for c in skus:
        if c not in costs.keys():
            return -1
        if c in basket:
            basket[c]+=1
        else:
            basket[c] = 1

    # First remove those free items
    for product in frees.keys():
        if product in basket.keys():
            freeItem = basket[product]//frees[product][0]
            # Tuple 1 shows the product code of free item
            if frees[product][1] in basket.keys():
                if basket[frees[product][1]] > freeItem:
                    basket[frees[product][1]] -= freeItem
                else:
                    basket.pop(frees[product][1])
    
    # Calculate cost
    total = 0 
    
    # Process any three offer
    # Looking at unit prices, any three for 45 will always be the cheapest option
    remaining = [] # The leftover products from previous item in buy any 3 group
    for product in anythree:
        if product in basket.keys():
            # Add products to remaining list and remove from basket
            remaining += [product for i in range(basket[product])]
            basket.pop(product)

            anythree_batch_size = len(remaining)//3
            total+=anythree_batch_size*45
            # Remove calculated products
            remaining = remaining[anythree_batch_size*3:]
    
    # Add anything as unit cost which was not part of buy any 3
    for r in remaining:
        total += costs[r]

                
    # Other items in basket
    for product in basket.keys():
        if product in discounted.keys():
            unit = basket[product]
            cost = 0
            # Buy x for this amount offer 
            for discount_info in discounted[product]:
                calculated_batch = unit//discount_info[0]
                if calculated_batch > 0:
                    unit -= calculated_batch * discount_info[0]
                    cost += calculated_batch * discount_info[1]
                    
            # Remaining units
            if unit !=0 :
                cost += unit * costs[product]
       
        else:
            # Use unit prices
            cost = basket[product] * costs[product]
           
        total += cost


    return total
