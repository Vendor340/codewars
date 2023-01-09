def digit_sum(n):
	sum_1 = 0
	n = str(eval(str(n)))
	for i in n:
		sum_1 += int(i)
	return sum_1
print(digit_sum(0))