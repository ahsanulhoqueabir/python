def bisection(f,a,b,TOL,N0):
    
    if f(a)*f(b) > 0:
        print('f(a)*f(b)>0. Bisection method cannot be applied.')
        return None
  
    i=1
    FA=f(a)
    print('   n         a               b              p            f(p)')
    print(' ----------------------------------------------------------------------')
    while (i<=N0):
        p=(a+b)/2
        FP=f(p)
        print(format(i,'>4d'),' ',format(a,'>12.8f'),' ',format(b,'>12.8f'),' ',format(p,'>12.8f'),' ',format(FP,'>12.8f'))
        if FP==0 or abs(f(p))<TOL:
            FP=f(p)
            return print('The solution is ',p)
        i=i+1
        if FA*FP>0:
            a=p
            FA=FP
        else:
            b=p
    print('Method failed after ',N0,' iterations')
    return None

f = lambda x: x**3 + 4*x**2 - 10
a = 1
b = 2
TOL = 1e-5
N0 = 100
bisection(f,a,b,TOL,N0)