class MaxSq:
    def __init__(self):
        self.prev = 0
        istr, jstr = input().split()
        self.i = int(istr)
        self.j = int(jstr)

        self.sumFin = [[0 for ii in range(self.j)] for jj in range(self.i)]
        
        for ii in range(self.i):
            line = input().split()
            # self.table.append(line)
            s = 0
            for kN in range(len(line)):
                k = line[kN]
                s += int(k)
                if(ii == 0):
                    self.sumFin[ii][kN] = s
                else: 
                    self.sumFin[ii][kN] = s + self.sumFin[ii - 1][kN]

    def checkZero(self, x, y):
        if(x==0 and y==0 and self.sumFin[x][y] == 0):
            return True
        if(x>0):
            if(self.sumFin[x][y] != self.sumFin[x-1][y]):
                return False
            return True
        if(self.sumFin[x][y] != self.sumFin[x][y-1]):
            return False
        return True

    def sumDiap(self, xa, ya, razm):
        razm -= 1
        if(xa + razm > self.i or ya + razm > self.j):
            return -1
        xymax = self.sumFin[xa+razm][ya+razm]
        if(xa == 0 and ya == 0):
            return xymax
        if(xa == 0):
            return xymax - self.sumFin[xa+razm][ya-1]
        if(ya == 0):
            return xymax - self.sumFin[xa-1][ya+razm]

        return(xymax+self.sumFin[xa-1][ya-1]-self.sumFin[xa-1][ya+razm]-self.sumFin[xa+razm][ya-1])
    

    def prSum(self):
        for ii in range(self.i):
                res = ''
                for jj in range(self.j):
                    res += ' ' + str(self.sumFin[ii][jj])
                print(res[1:])
    
    # Для заданной точки ищет максимальный квадрат
    def maxSquare(self, x, y, r=1):
        # print(x, y)
        if(self.checkZero(x, y)):
            return 0
        sqMin = r
        sqMax = min(self.i-x, self.j-y)
        while(sqMin < sqMax):
            # print(x, y, sqMin, sqMax)
            if(sqMin + 1 == sqMax):
                if(self.checkSqr(x, y, sqMax)):
                    return sqMax
                else:
                    return sqMin
            sqMed = (sqMin + sqMax) // 2
            if(self.checkSqr(x, y, sqMed)):
                sqMin = sqMed
            else:
                sqMax = sqMed
        return sqMin
    
    def checkSqr(self, x, y, n):
        return self.sumDiap(x,y,n) == n**2


    def allPrint(self):
        for ii in range(self.i):
            for jj in range(self.j):
                
                self.maxSquare(ii, jj)

    def getMaxFromSquare(self):
        mx = 0
        s = 0
        for t in range(min(self.i, self.j)):
            mxCand = self.maxSquare(t, t, mx)
            mx = max(mx, mxCand)
            if(mx >= min(self.i, self.j) - t):
                # print(s)
                return mx
            s += 1
            for i in range(t+1, self.i):
                # print(f'check {i}, {t}')
                mxCand = self.maxSquare(i, t, mx)
                mx = max(mx, mxCand) 
                s += 1            
                if(mx >= self.i-i):
                    break

            for j in range(t+1, self.j):
                # print(f'check {t}, {j}')
                mxCand = self.maxSquare(t, j, mx)
                mx = max(mx, mxCand)  
                s += 1            
                if(mx >= self.j-j):
                    break
        # print(s)
        return mx
                

m = MaxSq()
print(m.getMaxFromSquare())
