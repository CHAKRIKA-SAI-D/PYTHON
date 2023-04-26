import itertools
string="CAT"
perm_list=itertools.permutations(string)
print(list(perm_list))


output:
[('C', 'A', 'T'), ('C', 'T', 'A'), ('A', 'C', 'T'), ('A', 'T', 'C'), ('T', 'C', 'A'), ('T', 'A', 'C')]
