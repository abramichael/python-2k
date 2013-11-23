import os, random, time

class cellGen:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.array = []
        for i in range(m):
            self.array.append([])
        for i in range(m):
            for j in range(n):
                self.array[i].append(random.randint(0,1))
    def __str__(self):
        s = ""
        for i in range(self.m):
            for j in range(self.n):
                if self.array[i][j]==1:
                    c = 'x'
                else:
                    c = '.'
                s = s + str(c)
            s = s + "\n"
        return s
    def doIter(self):
        array2 = []
        for i in range(self.m):
            array2.append([])
        for i in range(self.m):
            for j in range(self.n):
                array2[i].append(self.trans(i,j))

        self.array = array2[:]
    def trans(self,i,j):
        s = 0
        for k in range(-1,2):
            for q in range(-1,2):
                s += self.array[(i+k+self.m)%self.m]\
                [(j+q+self.n)%self.n]
        if s > 5 or s == 4:
            return 1
        else:
            return 0

i = 0

c = cellGen(15,30)

while True:
    os.system("cls")
    print i
    print c
    time.sleep(0.01)
    c.doIter()
    i += 1
