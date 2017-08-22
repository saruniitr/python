#
# Python code exercises from CodeWars
# https://www.codewars.com/trainer/python
#

import sys
import functools
import math
import re
from collections import Counter

def isogram(str):
	""" A word in which no character is repeated """
	d = {};
	for c in str:
		if c not in d:
			d.update({c : 1});
		else:
			return False;

	return True;

def get_vowel_count(str):
	count = 0;
	vowels = set('aeiou');

	for c in str.lower():
		if c in vowels:
			count = count + 1;

	return count;

def tribonacci(signature, n):
    seq = signature.copy();
    for i in range(3, n):
        seq.append(seq[i - 3] + seq[i - 2] + seq[i - 1]);

    print(seq[0:n]);

def getmiddle(s):
    """returns middle character"""
    mid = len(s)//2;
    if (len(s) % 2) == 0:
        return s[mid-1:mid+1];
    else:
        return s[mid];

def array_diff(a, b):
    # remove all elements of list a that are present in b
    return [i for i in a if i not in b];

def persistence(n):
    # calculate how many times the digits of given number
    # are to be multiplied to reach a single digit
    # eg: 39 => 3*9 = 27 => 2*7 = 14 => 1*4 = 4, so 3 steps
    count = 0;
    while len(str(n)) > 1:
        n = functools.reduce(lambda x, y: int(x) * int(y), str(n))
        count = count + 1;

    return count;

def duplicate_count(text):
    d = Counter(text);

    count = 0;
    for k, v in d.items():
        count = count + (v > 1);

    return count;

def divisors(num):
    l = [ i for i in range(2, num) if not(num % i)];

    if len(l):
        return l;
    else:
        return '{0} is prime'.format(num);

def maskify(cc):
    str = cc;
    length = len(cc);
    if length > 4:
        m = '#' * (length - 4);
        str = cc.replace(cc[0:-4], m);

    return str;

def DNA_strand(dna):
    d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'};
    return ''.join([d[c] for c in dna])

def narcissistic(value):
    # if sum of power of each digit raised to length of number equals value
    # then it is narcissistic
    # eg: 153 = 1^3 + 5^3 + 3^3 = 153
    return sum([int(d)**len(str(abs(value))) for d in str(value)]) == value;

def dig_pow(n, p):
    # eg (89, 1) => 8^1 + 9^2 = 89 * 1 so output is 1
    length = len(str(abs(n)));
    powers = list(range(p, p+length))

    total = sum(int(i)**j for i, j in list(zip(str(n), powers)));

    if not(total % n):
        return total // n;
    else:
        return -1;

def find_missing_letter(chars):
    # chars is sequence of consecutive letters except that one
    # char is missing in the sequence, we need to find it
    return [str(chr(ord(y) - 1)) for x, y in list(zip(chars[:-1], chars[1:])) if (ord(y) - ord(x)) > 1][0]

def compare(array1, array2):
    if (array1 is None) or (array2 is None):
        return False;

    a = set(array1)
    b = set([math.sqrt(i) for i in array2])

    return ((len(a) == len(b)) and (len(a - b) == 0))


def valid_parenthesis(str):
    count = 0;

    for i in str:
        if i == '(':
            count += 1;
        if i == ')':
            count -= 1;
        if count < 0:
            return False;

    return count == 0;



def practice():
    # print(get_vowel_count('abracadabra'));
    # tribonacci([1, 1, 1], 1);
    # print(DNA_strand ("GTAT"));


if __name__ == "__main__":
    practice();
