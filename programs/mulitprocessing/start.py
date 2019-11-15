import multiprocessing as m
import time

start = time.perf_counter()

def do1():
	print("sleeping 1 second...")
	time.sleep(1)

# do()

# with multiprocessing

p1 = m.Process(target=do1)
p2 = m.Process(target=do1)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# finish -> 1.1,1.4,1.8 time consuming as per your system process
# finish-start ->1.0 always

