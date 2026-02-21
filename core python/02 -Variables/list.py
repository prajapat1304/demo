a = [5,10,15,20,25,30,35,40,45,50]
#print("a[2]=",a[2])
#a[1] = 10
a1=(5,10,15,20,25,30,35,40,45,50,55)
print(a.__sizeof__())
print(a1.__sizeof__())
a.append(11)
print(a)
print("length =",len(a))
del a[1]
print(a)

b =['ram','shyam','1','2','a']
print(b[-1])