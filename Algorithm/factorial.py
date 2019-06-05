def crazylaoba(a):
    if a == 1:
        return 1
    else:
        return crazylaoba(a - 1) + a
    
