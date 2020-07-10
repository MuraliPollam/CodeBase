def ugly(n):
    uglylist = []
    uglylist.append(1)
    for i in range(1,n):
        uglylist.append(0)
    two_multiple=2
    three_multiple=3
    five_multiple=5
    a1=a2=a3=0

    for i in range(1,len(uglylist)):
        num=min(two_multiple,three_multiple,five_multiple)
        uglylist[i]=num
        if num == two_multiple:
            a1=a1+1
            two_multiple=uglylist[a1]*2
        if num == three_multiple:
            a2=a2+1
            three_multiple=uglylist[a2]*3
        if num == five_multiple:
            a3=a3+1
            five_multiple=uglylist[a3]*5

    return uglylist[n-1]
n=int(input())
print(ugly(n))

