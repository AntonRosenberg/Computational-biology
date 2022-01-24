import numpy as np
import matplotlib.pyplot as plt
from ddeint import ddeint


def equation(N, t):
    return r * N(t) * (1 - N(t-delay)/K)*(N(t)/A-1)

def initial_history_func_0(t):
    return N0

def detectoscillation(X):
    dx = np.diff(X)
    return not np.all(dx >= -0.001)

if __name__ == '__main__':
    global r, A, K, N0
    r=0.1
    A=20
    K=100
    N0=50

    T = [0.1*_ for _ in range(1, 51)]
    ts = np.linspace(0, 50, 5000)
    Ns=[]

    global delay

    for delay in T:
        Ns.append(ddeint(equation, initial_history_func_0, ts))

    for i, sol in enumerate(Ns):
        plt.plot(ts, sol, linewidth=1, label=f'delay = {T[i]}')
        if detectoscillation(Ns[i])==True:
            Tcritical = T[i]
            break

    print(Tcritical)

    #plt.legend(loc="upper left")
    plt.show()
