# Prime sieve.

from typing import List

def sieve_gen(n: int) -> List[int]:
  """Prime sieve.
    
  Find all prime numbers up to n.
  Uses generator to return the primes.
  """
  a = [False, False] + [True] * (n - 1)
	i = 2
	while (j := i**2) and j <= n:
		if a[i]:
			yield i
			for k in range(j, n + 1, i):
				a[k] = False
		i += 1

	for x in [idx for idx, x in enumerate(a)
						if x == True and idx * idx > n]:
			yield x

if __name__ == "__main__":
	n = 10 ** 8
	for i in sieve_gen(n):
		print(i)