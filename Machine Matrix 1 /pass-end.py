import string
from itertools import permutations

alphabet_lc = alphabet = list(string.ascii_lowercase)
alphabet_uc = list(string.ascii_uppercase)
numbers = [str(i) for i in range(0, 10)]
symbols = list(string.punctuation)
all_chars = alphabet_lc + alphabet_uc + numbers + symbols

pass_1 = 'k1ll0r'
perms = list(permutations(all_chars, 2))
for perm in perms:
	comb_perm = perm[0] + perm[1]
	pass_upd = pass_1 + comb_perm
	print(pass_upd)
