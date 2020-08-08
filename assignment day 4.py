def search(a,lst,n):
    s = len(lst)
    k = -1
    for i in range(n+1,s):
        if a == lst[i]:
            k = i
            break
    return k
n = int(input("Enter number of elements in list?"))
lst = []
print("Enter elements one by one:")
for i in range(0,n):
	d = int(input())
	lst.append(d)
a = [1,1,5]
n1 = search(a[0],lst,-1)

n2 = search(a[1],lst,n1)

n3 = search(a[2],lst,n2)
if (n1 >= 0 and n2 >= 0 and n3 >= 0) and (n1 < n2 and n2 < n3):
    print("it's a Match")
else:
    print("it's gone.")