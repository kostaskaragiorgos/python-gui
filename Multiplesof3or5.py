def sumofm3or5():
    sum = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            print("the",i,"is multiple of 3 or 5")
            sum +=i
    return sum

print("The sum of all the multiples of 3 or 5  below 1000 is",sumofm3or5())