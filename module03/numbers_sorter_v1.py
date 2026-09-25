n = []
while True:
    inputs = input('Inputs your number to sort or end to finish')
    if inputs == 'end':
        print('ended')
        break
    x = float(inputs)
    n.append(x)
sn = n.copy()
o = False
oi = []
while o == False:
    for i in range(1,len(sn)):
        ni1 = sn[i-1]
        ni2 = sn[i]
        if ni1 > ni2:
            sn[i-1] = ni2
            sn[i] = ni1
            o = False
            print(o, n, sn)
            break
        else:
            o = True
print(o, n, sn)
