def str_rev(s):
    a=["a","e","i","o","u"]
    l=list(s)
    for i in l:
        if i in a:
            l.remove(i)
    return"".join(l)
