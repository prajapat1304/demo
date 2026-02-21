#CREATING TUPLE
my_tuple = ()
print(my_tuple)

#tuple of int, string, float
tuple_list1 = (1,2.8,"Hello Ram")
print(tuple_list1)
print(len(tuple_list1))

#tuple of string and list
tuple_list2 = ("book",[2,4,6,8])
print(tuple_list2)

print(tuple_list2[0:1])

t =tuple_list1 + tuple_list2
print(t)
t1 = tuple_list1 * 2
print(t1)

#Accessing elements from nested tuples
tuple_list3 = (1,"balram",(11,22,33))
print(tuple_list3[1][2])
print(tuple_list3[2][1])