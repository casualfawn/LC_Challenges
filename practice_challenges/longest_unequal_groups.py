prices = [7,1,5,3,6,4]

maxp = max(prices)
minp = min(prices)

for i in range(len(prices)):
    if prices[i] == minp:
        selldays = prices[i:len(prices)-1]
res = max(selldays) - minp