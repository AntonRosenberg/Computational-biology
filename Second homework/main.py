import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    L = 100
    rho = 0.5
    q = 8
    eps_0 = 20
    dt = 0.01
    t_max = 1000
    u0 = (q-1)/2 + np.sqrt(((q-1)/2)**2+q/rho-q)

    u = [[0 for i in range(L)] for j in range(int(t_max/dt))]
    u[0][:] = [u0/(1+np.exp(i-eps_0)) for i in range(L)]

    for i in range(int(t_max/dt)-1):
        for j in range(L):
            if j == 0:
                u[i+1][j] = u[i][j]
            elif j == L-1:
                u[i+1][j] = u[i][j]
            else:
                u[i+1][j]=(rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1-u[i][j]) + u[i][j-1]+u[i][j+1]-2*u[i][j])*dt+u[i][j]

    #for t in range():
    #    plt.plot(u[t*2000][:], label=f't={t*2000*dt}')
    plt.plot(u[2000][:], label=f't=0')
    plt.plot(u[4000][:], label=f't=last')
    plt.legend()
    plt.show()

