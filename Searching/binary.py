list=[2,3,4,5,6,8,9]
num=int(input())
low=0
high=len(list)-1
mid=(low+high)//2
while(num!=list[mid] and high!=low):
    print(mid,"mid")
    if(num>list[mid]):
        low=mid+1
    else:
        high=mid-1
    mid=(low+high)//2
if(num==list[mid]):
    print("matched")
else:
    print("not matched")
