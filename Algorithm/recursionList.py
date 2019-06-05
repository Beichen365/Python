def com(things, x):
    if len(things) == 0:
        print(x)
    else:
        for thing in things:
            curx = x
            curx += str(thing)
            things2 = things.copy()
            things2.remove(thing)
            com(things2, curx)
            
com([1, 2, 3, 4], "")
