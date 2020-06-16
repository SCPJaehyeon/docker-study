from random import *

def gen_randon(n):
	res = []
	for i in range(n):
		res.append(randint(1, n))
	return res
	

def sorted_random(n):
	res = []
	for i in range(n):
		res.append(randint(1, n))
	res = quick_sort(res)
	return res

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    p = lst[len(lst) // 2]
    less = []
    same = []
    great = []
    for n in lst:
        if n > p:
            great.append(n)
        elif n < p:
            less.append(n)
        else:
            same.append(n)
    return quick_sort(less) + same + quick_sort(great)

def main():
    n = int(input())
    res_fir, res_sec = [], []
    res_fir = gen_randon(n)
    res_sec = sorted_random(n)
    print(res_fir)
    print(res_sec)


if __name__ == '__main__':
    main()

