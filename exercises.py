#
# Python code exercises from CodeWars
# https://www.codewars.com/trainer/python
#

import sys
import functools
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


def practice():
    # print(get_vowel_count('abracadabra'));
    # tribonacci([1, 1, 1], 1);
    print(DNA_strand ("GTAT"));

if __name__ == "__main__":
    practice();
