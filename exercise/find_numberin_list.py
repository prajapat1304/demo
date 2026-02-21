list=[10,20,23,27,33,34,44,55,68]
number = 21
count = 0
for i in list:
    if i == number:
        count +=1
if number in list:
    print("number is in the list")
else:
    print("number is not in list")