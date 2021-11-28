# Merge sort implementation using Fuctional Programming.
# Uses Python 3.10 match statement.

from typing import List

def merge (x: List[float], y: List[float]) -> List[float]:
	match x, y:
		case [], y:
			return y
		case x, []:
			return x
		case x, y if x[0] <= y[0]:
			return [x[0]] + merge(x[1:], y)
		case x, y:
			return [y[0]] + merge(x, y[1:])

def msort(s: List[float]) -> List[float]:
	"""Sort the given integer list in the ascending order."""

	match s:
		case []:
			return []
		case [x]:
			return [x]
		case s:
			half = len(s) //2
			return merge(msort(s[:half]), msort(s[half:]))

if __name__ == "__main__":
	seqs = [
		[4, 3, 1, 2],
		[8, 2, 4, 10, 6, -5, -20],
		[10.5, 8.5, -32, -1.75, 9, 5.5],
		[True, False, True, False],
	]

	for s in seqs:
		sorted = msort(s)
		print(f"Original list\t= {s}")
		print(f"Sorted list\t= {sorted}")

# Sample output

"""
$ python -m sort

Original list = [4, 3, 1, 2]
Sorted list = [1, 2, 3, 4]
Original list = [8, 2, 4, 10, 6, -5, -20]
Sorted list = [-20, -5, 2, 4, 6, 8, 10]
Original list = [10.5, 8.5, -32, -1.75, 9, 5.5]
Sorted list = [-32, -1.75, 5.5, 8.5, 9, 10.5]
Original list = [True, False, True, False]
Sorted list = [False, False, True, True]
"""