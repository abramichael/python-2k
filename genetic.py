import string, random, time

name = "MICHAEL"

def f(s):
    global name
    d = 0
    for i in range(len(name)):
        d += abs(ord(s[i]) - ord(name[i]))
    return d
        

def sort(p):
    for i in range(len(p)-1):
        min = p[i]
        kmin = i
        j = i + 1
        while (j<len(p)):
            if f(p[j])<f(min):
                min = p[j]
                kmin = j
            j += 1
        h = p[i]
        p[i] = p[kmin]
        p[kmin] = h

def crossover(p):
    i = 0
    h = len(p[0])/2
    while (i<len(p)/2):
        s3 = ""
        s4 = ""
        for j in range(len(p[0])):
            if (j % 2 == 0):
                s3 = s3 + p[i][j]
                s4 = s4 + p[i+1][j]
            else:
                s4 = s4 + p[i][j]
                s3 = s3 + p[i+1][j]
                
        p.append(s3)
        p.append(s4)
        i += 2

def mutation(p):
    
    i = random.randint(0, len(p)-1)
    s = p[i]
    print s

    j = random.randint(0,len(s)-1)
    c = chr(((ord(s[j]) + 1) % 26) + 65)
    s = s[:j] + c + s[j+1:]
    p[i] = s
    print s

p = []
for i in range(500):
    p.append(''.join(random.choice(string.ascii_uppercase) \
            for x in range(len(name))))
print p
k = 0
while (k < 500):
    sort(p)
    print "# " + str(k)
    print p[0]
    p = p[:len(p)/2 + 1]
    random.shuffle(p)
    crossover(p)
    
    p = p[len(p)/2:]
    random.shuffle(p)
    crossover(p)
    mutation(p)
    #print p
    #print p
    k += 1
    time.sleep(2)
