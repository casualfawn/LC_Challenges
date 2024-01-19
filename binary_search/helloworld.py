
import time

strs = ' abcdefghijklmnopqrstuvwxyz'
helloworld = [s for s in 'Send nudes']
helloworldlett = 'Send nudes'
strs = [s for s in strs]
row = len(helloworld)
sf = helloworld[0]
for j in range(0,3):
    if sf == helloworldlett:
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
        time.sleep(.04)
        print(sf)
    sf = helloworld[0]
    for i in range(1, row):
        for l in strs:
            time.sleep(.03)
            if l == helloworld[i]:
                sf += l
                print(sf, sep = '')
                break
            else:
                print(sf, l, sep='')
                sf = sf
