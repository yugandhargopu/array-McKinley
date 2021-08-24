size=int(input("ENTER ARRAY SIZE"))

arr=[]

for i in range(size):

    element=int(input())

    arr.append(element)

print("largest number is",max(arr))
print("smallest number is",min(arr))