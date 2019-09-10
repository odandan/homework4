# create a list of thr first 100 numbers
x = list (range(2, 100+1))
for i in x:
    j=2
    while (i * j <= x[-1]):
    if (i * j in x ) :
        x.remove