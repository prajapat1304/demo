name ="Mera name pushpa hai"
for char in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for letter in name:
        if char == letter:
            count +=1
            if count>0:
                print(char,"count =",count)