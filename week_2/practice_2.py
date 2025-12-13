"""2, You are given a list of product prices:
prices = [120, 45, 300, 85, 150]
Write a function get_expensive_products(prices) that returns a new
list containing only the prices greater than 100."""

def get_expensive_products(prices):
    expensive = []
    for price in prices:
        if price > 100:
            expensive.append(price)
    return expensive
prices = [120, 45, 300, 85, 150]

# Call the function 
result = get_expensive_products(prices)
print(result)
