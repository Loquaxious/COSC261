def shuffle(s, t):
    """Returns the shuffle S||T of strings s and t"""
    s_set = set()
    t_set = set()
    if len(s) == 0:
        return {t}
    elif len(t) == 0:
        return {s}
    else:
        s0 = s[0]
        t0 = t[0]
        
        for s_string in shuffle(s[1:], t):
            s_set.add(s0 + s_string)
        for t_string in shuffle(s, t[1:]):
            t_set.add(t0 + t_string)
        
    return s_set.union(t_set)

    
print(sorted(shuffle('ab', 'cd')))  
print(sorted(shuffle('', 'e')))   