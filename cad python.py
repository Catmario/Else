import math
pi = math.pi
global r1,r1x,r1y
r1 = 5.55
s_px = 230
s_py = 180
r1x = s_px - r1 * math.cos(1.0/12*pi)
r1y = s_py + r1 * math.sin(1.0/12*pi)
Max_L = 3
Max_H = 2

def inputForce():
    stopword = ''
    Force = []
    print 'input 5 or 15 nums :(end by double enter)'
    for line in iter(raw_input, stopword):
        try:
            Force.append(float(line))
        except:
            print 'pls input the correct num'
            Force = []
    if len(Force) not in {5,15}:
        print 'num not in {5,15}'
        exit()
    print Force
    return Force

def tunnel(s_px,s_py):
    print 'pline %d,%d' % (s_px,s_py)
    print 'a'
    print 'r ' + str(r1)
    print 'a 210'
    print '180'
    print 'r 15'
    print '%d,%d' % (s_px,s_py)
    print ''
    print ''
    
def gs(Force,Max_L):
    tha = [180,135,90,45,0]
    F_abs = map(abs,Force)
    L = map(lambda x: float('{:.2f}'.format(x/max(F_abs)*Max_L)),F_abs)
    j = 0
    for i in L:
        print 'L %.2f,%.2f' % (r1x,r1y)
        print '@%.2f<%d' % (i+r1,tha[j])
        print ''
        print ''
        j = j + 1

def cf(Force,Max_L,Max_H):
    L = map(lambda x: float('{:.2f}'.format(x/max(Force)*Max_H)),Force)
    j = 0
    tha = [180,135,90,45,0]
    dis = [1.0/6,1.0/2,5.0/6]
    for i in L:
        if j % 3 == 0:
            print 'L %.2f,%.2f' % (r1x,r1y)
            print '@%.2f<%d' % (Max_L+r1,tha[j/3])
            print ''
            print ''
        x = r1x + (r1 + Max_L * dis[j%3]) * math.cos(tha[j/3]/180.0*pi)
        y = r1y + (r1 + Max_L * dis[j%3]) * math.sin(tha[j/3]/180.0*pi)
        print 'L %.2f,%.2f' % (x,y)
        print '@%.2f<%d' % (i,tha[j/3]-90)
        print ''
        print ''
        j = j + 1

    
print 'gs 1 cable 0'
gsornot = float(raw_input())
if gsornot == 1:
    print '------ gs mode ------'
    Force = inputForce()
elif gsornot == 0:
    print '------ cable mode ------'
    Force = inputForce()
else:
    print 'pls choose the mode'
    exit()
    
print '--------------------------'
print '-----------copy-----------'
tunnel(s_px,s_py)
if gsornot == 1:
    gs(Force,Max_L)
else:
    cf(Force,Max_L,Max_H)
print '-------- copy end---------'
print '--------------------------'
