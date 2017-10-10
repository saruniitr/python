#
# Useful Python snippets/questions
#

import functools
import math
from collections import namedtuple

# Dictionary comprehension
print('\nDictionary comprehension')
d = {(x, x**2) for x in range(11)}
print('list of squares as dict,\nd = ', d)



# Lists and Slicing
print('\nLists and Slicing')
l = [x for x in range(1, 11)]
print('original list: ', l)
print('every other element, list[::2]: ', l[::2])
print('every third element, list[::3]: ', l[::3])
print('reverse of list, list[::-1]: ', l[::-1])
print('sum of even numbers: ', \
	  functools.reduce(lambda x, y: x + y, filter(lambda x: not (x % 2), l)))
print('sum of odd numbers: ', \
	  functools.reduce(lambda x, y: x + y, filter(lambda x: (x % 2), l)))


# flattening of lists
print('\nFlattening of Lists')
l = [[1, 2], [3, 4], [4, 6], [8, 10], [5, 9]];
print('list l: ', l);
print('flattened list: sum(l, []) - **** very inefficient ****:', sum(l, []));
print('flattened using list comprehension:',
	  [x for l1 in l for x in l1]);


# zip and unzip
print('\nzip and unzip')
team = ['a', 'b', 'c', 'd', 'e']
score = [40, 50, 35, 50, 45]
l = list(zip(team, score))
print('list of zip: ', l)
print('unzip: ', list(zip(*l)))


def remove_duplicates():
	"""
	removing duplicates in a list
	"""
	l = [5, 6, 5, 5, 1, 2, 3, 4, 4, 9, 8, 3, 12, 14, 7, 10, 20, 8]
	print('original list:', l)
	# method1 - using set() but it changes the order
	print('Method1 using set() but it changes order:', list(set(l)))

	# method 2 - doesn't change order
	unique = []
	visited = set()
	for x in l:
		if x not in visited:
			unique.append(x)
			visited.add(x)

	print('Method2 with order restored:', unique)

def named_tuples():
	"""
	Demonstrates named tuples which are like struct in C
	where in we can define a tuple with a name and give names
	to the members as well
	"""
	Point = namedtuple('Point', 'x y')

	pt1 = Point(1, 0)
	pt2 = Point(4, 4)

	distance = math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
	return distance

if __name__ == "__main__":
	print(named_tuples())
