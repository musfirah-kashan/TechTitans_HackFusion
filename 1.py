import random
choice=random.randint(1,50)
print(choice)
n=int(input())
target=n-1
count=0
while target!=choice:
    if n==choice:
        count+=1
        print(f"Correct! you guesses it in {count} attempts")
        target+=1
        break

    elif n>choice:
        count+=1
        print(f"That's above the target!")
        n=int(input())

    else:
        count+=1
        print("That's below the target!")
        n=int(input())

   

