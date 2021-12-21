# calculating pi
# by DuskyElf

pi = 0
count = 1
negative = False

while True:
    for i in range(10000000):
        if negative:
            pi -= 1/count
        else:
            pi += 1/count
        
        count += 2
        
        negative = not negative

    print(pi*4)
    print(count)
    
