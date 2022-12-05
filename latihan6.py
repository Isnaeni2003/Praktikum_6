import math

def a(x):
  return lambda a : a + x**2
hasil = a(2)
print(hasil(11))

def b(x,y):
	return math.sqrt (x**3 + y**2)
hasil = b(2,1)
print(hasil)

def c(*args):
	return sum(args)/len(args)
hasil = c(1,2,3,4,5)
print(hasil)

def d(s):
	return "@".join(set(s))
hasil = d(['k','koo','jnjj'])
print(hasil)



