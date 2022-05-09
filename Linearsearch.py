def linearsearch(list1,key):
    list2 = []
    flag = False
    for i in range(len(list1)):
        if key == list1[i]:
            flag = True
            list2.append(i)
    if flag==True:
        print("key element is found at index",i)
        for i in list2:
            print(i)
    else:
        print("element is not found")
list1 =[]
n=int(input("Enter number of elements :"))
print("Enter the list of elements:")
for i in range(0,n):
    m=int(input())
    list1.append(m)
list1.sort()
print(list1)
key = int(input("enter the key :"))
linearsearch(list1,key)