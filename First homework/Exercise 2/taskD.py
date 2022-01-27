import numpy as np
import matplotlib.pyplot as plt 

def model(init_pop,iter):
    N = init_pop
    a = []
    a.append(N)
    for i in range(iter):
        N = (r+1)*N/(1+np.power(N/k,b))
        a.append(N)
    plt.loglog(a,c='tab:green',label=['Exact dynamics','','',''])

    return N

def linear_approx(init_pop, fix_point, iter):
    f_prime = ((r+1)*(1+np.power(fix_point/k,b)) - b*(r+1)*np.power(fix_point/k,b)) / (1 + np.power(fix_point/k,b))**2
    a = []
    for i in range(iter):
        a.append( fix_point + f_prime**i * init_pop )
    return a
    

if __name__ == '__main__':
    k = 10**3
    r = 0.1
    b = 1
    n0 = np.array([1,2,3,10])
    dn0 = np.array([-10,-3,-2,-1,1,2,3,10])
    iter = int(2*10**2)
    fp1 = 0
    fp2 = k*np.power(r,1/b)

    print(model(n0,iter))


    aprx = linear_approx(n0,fp1,iter)
    plt.loglog(aprx,'--',c='tab:blue',label=['Approx dynamics','','',''])

    #aprx = linear_approx(dn0,fp2,iter)
    #plt.loglog(aprx,'--',c='tab:blue',label=['Approx dynamics','','','','','','',''])

    plt.legend()
    plt.xlabel('Generation \u03C4')
    plt.ylabel('Population N')
    plt.show()
