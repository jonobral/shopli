"""Automated Shopping List"""
with open('products_list.txt') as products:
    for line in products:
        print line
        if 'str' in line:
            break
