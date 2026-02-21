number = int(input("Enter a number:"))
count =0
for i in range(2,number):
    if number%i==0:
        count +=1

if count ==0:
    print("prime number:",number)
else:
    print("NOT a prime number:",number)