def all_subsets(s):
    """ """
    if len(s) == 0:
        return [set()]
    else:
        s0 = s.pop()
        results = all_subsets(s)
        new_lst = []
        for sets in results:
            new_lst.append(sets.union({s0}))
        return new_lst + results

print(sorted(map(sorted, all_subsets({0, 1, 2}))))