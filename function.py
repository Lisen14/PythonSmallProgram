def fibs(num):
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2]+result[-1])
	return result

print fibs(100)


def with_star(**kwds):
	print kwds['name'], 'is' , kwds['age']

x={"aa":1,"bb":2}

with_star(aa = 1,bb = 2)


