# Sieve of Erastothenes
# Cs. https://www.geeksforgeeks.org/sieve-of-eratosthenes/

from typing import List

def sieve(n: int) -> List[int]:
  """Prime sieve.

  Given a prime number,
  it strikes out" all composites of that prime number up to n.

  Starting from the smallet prime number,
  it repeats this process for all the prime numbers up to sqrt(n).
  """
  a = [False, False] + [True] * (n - 1)
  i = 2
  while (j := i**2) and j <= n:
    if a[i]:
        yield i
        for k in range(j, n + 1, i):
          a[k] = False
  	i += 1

	return [idx for idx, x in enumerate(a) if x == True]

if __name__ == "__main__":
	n = 1000
	a = sieve(n)
	print(a)