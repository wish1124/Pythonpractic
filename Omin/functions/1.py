def addInterest(balance, rate):
    for i in range(len(balance)):
        balance[i] = balance[i] * (1 + rate)
        
def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)
    
test() # [1050.0, 2310.0, 840.0, 378.0]



