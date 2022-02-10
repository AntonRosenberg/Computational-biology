import numpy as np
import matplotlib.pyplot as plt
from ddeint import ddeint


def equation(N, t):
    return r * N(t) * (1 - N(t-delay)/K)*(N(t)/A-1)


def initial_history_func(t):
    return N0


def detect_oscillation(X):
    dx = np.diff(X)
    return not np.all(dx >= -1e-3)

def detect_limitcycle(X):
    X = round(X,3)
    max1=X[argrelextrema(X, np.greater)[0]]
    max2=X[argrelextrema(X, np.greater)[1]]
    if round(max1/max2,2)==1:
        return True
    return False

if __name__ == '__main__':
    global r, A, K, N0
    r=0.1
    A=20
    K=100
    N0=50

    T = [0.1*_ for _ in range(30, 45)]

    tmax = 800
    ts = np.linspace(0, tmax, 100*tmax)
    Ns = []

    global delay

    for delay in T:
        Ns.append(ddeint(equation, initial_history_func, ts))

    plt.subplot(1, 2, 1)

    for i, sol in enumerate(Ns):
        plt.plot(ts, sol, linewidth=1, label=f'delay = {round(T[i],1)}')
        '''
        if detect_oscillation(Ns[i])==True:
            Tcritical = T[i]
            break
        '''
    plt.title('N(t)')
    plt.xlabel('t')
    plt.ylabel('N(t)')
    plt.legend(loc="lower right")

    for i,sol in enumerate(Ns):
        if detect_limitcycle(Ns[i])==True:
            Tcritical = T[i]
            break
    '''
    for i,sol in enumerate(Ns):
        if detect_oscillation(Ns[i])==True:
            Tcritical = T[i]
            break
    '''
    print(f'Tcritical = {Tcritical}')

    plt.subplot(1, 2, 2)
    Ndot = np.zeros([len(Ns), len(Ns[0])])
    for i, sol in enumerate(Ns):
        for t in range(len(sol)):
            if t-100*delay>0:
                Ndot[i,t] = r * sol[t] * (1 - sol[round(t-100*T[i])]/K)*(sol[t]/A-1)
            else:
                Ndot[i,t] = r * sol[t] * (1 - N0 / K) * (sol[t] / A - 1)
        '''
        Nrounded = [round(value,5) for value in Ndot[i,:]]
        if len(set(Nrounded)) != len(Nrounded):
            Tcritical = T[i]
            break
        '''
        plt.plot(sol, Ndot[i,:], label=f'delay = {round(T[i],1)}')
    plt.title('dN/dt')
    plt.xlabel('N(t)')
    plt.ylabel('dN/dt')
    #print(Tcritical)
    plt.legend(loc="lower left")
    plt.show()
