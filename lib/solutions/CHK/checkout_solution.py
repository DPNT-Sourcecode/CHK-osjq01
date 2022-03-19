

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    costs = {'A':50, 'B':30, 'C':20, 'D':15}
    dict = {}
    for c in skus:
        dict[c]+=1

    # Calculate cost
    total = 0
    for product in ['A', 'B','C', 'D']:
        total += dict[product] *costs[product]

    return total



