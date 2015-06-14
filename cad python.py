import math
pi = math.pi
global r1,r1x,r1y
r1 = 5.55
s_px = 200
s_py = 200
r1x = s_px - r1 * math.cos(1.0/12*pi)
r1y = s_py + r1 * math.sin(1.0/12*pi)
Max_L = 3

def inputForce():
    stopword = ''
    Force = []
    print 'input 5 nums :(end by double enter)'
    for line in iter(raw_input, stopword):
        try:
            Force.append(float(line))
        except:
            print 'pls input the correct num'
            Force = []
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
    
def stress(Force,Max_L):
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

Force = inputForce()
print '--------------------------'
print '-----------copy-----------'
tunnel(s_px,s_py)
stress(Force,Max_L)
print '-------- copy end---------'
print '--------------------------'
