number = [i for i in range(1, 1001) if True in [True for j in range(2, 10) if i % j == 0]]
print(number)