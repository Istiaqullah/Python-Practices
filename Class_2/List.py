my_list=[5,7,6,8,4,1,2]
print("Without loop:-",end=" ")
print(*my_list)

print("----------------------------")
print("With loop:-",end=" ")
for i in range (len(my_list)):
    print(my_list[i],end=" ")
print()

print("----------------------------")
print("With loop & without range:-",end=" ")
for i in my_list:
    print(i,end=" ")

print()
print("----------------------------")

my_list.append("3.1416")               #append(appending in any index is not easy)
my_list.append("Pi")
my_list.insert(0,True)  #easy to add at any index
print(*my_list)

my_list.pop()                   #Pop
print(*my_list)

my_list.pop(0)                  #pop from an index
print(*my_list)

my_list.remove(1)
print(*my_list)


