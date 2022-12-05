

for a in range(1000):
    for b in range(1000-a):
        c = 1000 - a -b
        if c*c == b*b + a*a and a<b<c:
            print(a*b*c)
            break
