## Python tip!
## Recursive implementations of builtin min/max functions.
## Note that the min, max functions are overloaded
##  and they can take iterables or var arguments.
## We only implement these functions
##  for the List[float] arguments.

from typing import List, Optional

def find_min(s: List[float]) -> Optional[float]:
	"""Find the smallest value in the given list."""

	match s:
		case []:
			return
		case [h, *ts]:
			return (h if (m := find_min(ts)) is None
							or h <= m else m)

def find_max(s: List[float]) -> Optional[float]:
	"""Find the largest vallue in the given list."""

	match s:
		case []:
			return
		case [h, *ts]:
			return (h if (m := find_max(ts)) is None
							or h >= m else m)


if __name__ == "__main__":
	seqs = [
	  [4, 3, 1, 2],
		[8, 2, 4, 10, 6, -5, -20],
		[10.5, 8.5, -32, -1.75, 9, 5.5],
		[15, 10, 10, 5, 15, 5, 20, 10],
		[True, False, True, False],
	]
	for s in seqs:
		mn, mx = find_min(s), find_max(s)
		print(f"Input List\t= {s}")
		print(f"Min value\t= {mn}")
		print(f"Max value\t= {mx}")

# Sample output
"""
$ python -m min_max

Input List = [4, 3, 1, 2]
Min value = 1
Max value = 4
Input List = [8, 2, 4, 10, 6, -5, -20]
Min value = -20
Max value = 10
Input List = [10.5, 8.5, -32, -1.75, 9, 5.5]
Min value = -32
Max value = 10.5
Input List = [15, 10, 10, 5, 15, 5, 20, 10]
Min value = 5;
Max value = 20;
Input List = [True, False, True False]
"""