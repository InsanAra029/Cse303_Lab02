# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single
# digit any of the numbers is divisible by
highest={num: max([divisor for divisor in range(1,10) if num % divisor == 0])for num in range(1,1001)}
print(highest)