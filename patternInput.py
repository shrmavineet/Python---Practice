output = int(input("Enter the number: "))
count = 15
for i in range(output,0,-1):
    print(" " * (output-i),end="")
    for j in range(i):
        print(count, end=" ")
        count-=1
    print("")



    