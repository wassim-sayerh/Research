from random import randint

import time
start_time = time.perf_counter()


ntimes = int(input("How many times do you want to play? "))

success = 0

for i in range(ntimes):
    i = randint(0, 12)
    j = randint(0, 12)
    n = int(input(str(i) + " * " + str(j) + " = "))
    if n == i*j: success += 1
    while n != i*j:
        n = int(input("WRONG! " + str(i) + " * " + str(j) + " = "))
                
elapsed_time = time.perf_counter() - start_time
print("Grade:", str(success/ntimes*100) + "%")
print("Elapsed time:", round(elapsed_time, 2))
print("Time per question:", round(elapsed_time/ntimes, 2))
