import multiprocessing as m

def some():
	print("call nu7process")

p = m.Process(target=some)
p.start()