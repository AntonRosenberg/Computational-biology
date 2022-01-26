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


if __name__ == '__main__':
    global r, A, K, N0
    r=0.1
    A=20
    K=100
    N0=50

    T = [0.1*_ for _ in range(12, 22)]
    ts = np.linspace(0, 50, 5000)
    Ns=[]

    global delay

    for delay in T:
        Ns.append(ddeint(equation, initial_history_func, ts))

    for i, sol in enumerate(Ns):
        plt.plot(ts, sol, linewidth=1, label=f'delay = {round(T[i],1)}')
        if detect_oscillation(Ns[i])==True:
            Tcritical = T[i]
            break

    print(f'Tcritical = {Tcritical}')

    plt.legend(loc="lower right")
    plt.show()
