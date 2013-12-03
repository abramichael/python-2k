import string

def b():
    i = 0
    while (i<1024):
        s = bin(i)
        s = s[2:]
        s = string.zfill(s, 10)
        yield s
        i += 1

def c(b):
    for s in b:
        if string.count(s,"1") > 4:
            yield s

cc = c(b())
print cc.next()
print cc.next()
print cc.next()
