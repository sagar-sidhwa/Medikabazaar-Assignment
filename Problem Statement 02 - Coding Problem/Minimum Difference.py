#Minimum Difference
import sys
print(" *Note \n1. Enter minimum 2 Elements \n2. If there are 2 Elements then it cannot be same(for e.g 411 411)\n")
a=[int(ele) for ele in input("Enter the List of Elements\n").split()]

if (len(a)==0):
    print("No Data Entered")
elif (len(a)==1):
    print("Only One Car Speed Entered")
else:
    if(len(a)==2)and a[0]==a[1]:
        print("2 Cars Having Same Model")
    else:
        a=set(a)
        a=list(a)
        a.sort()
        d=sys.maxsize
        a1=0
        a2=0
        for i in range(len(a)-1):
            tmp = a[i+1]-a[i]
            if(d>tmp):
                d = tmp
                a1=a[i]
                a2=a[i+1]
            else:
                pass
        print(a1,a2,d)



