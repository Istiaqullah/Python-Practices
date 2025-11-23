my_set={1,2,3,4,4,4,5,6,5,8}
print(my_set)

my_set.add(99)
print(my_set)
if 5 in my_set:
    print("5 is present")
my_list=[1,2,3,4,5,5,5,2,3,0]
print(my_list)
new_set=set(my_list)             #List to set
new_list=list(new_set)           #set to list
print("new list:",new_list)
print(new_set)