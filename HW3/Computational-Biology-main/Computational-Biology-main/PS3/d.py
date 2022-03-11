from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

if __name__ == '__main__':
    b_n = 10
    d_n = 5
    pop = 100
    n_runs = 50000
    dt = 0.01

    freq_b = []
    freq_d = []

    for i in trange(n_runs):
        n = pop
        t = dt
        while n == pop:
            r = np.random.rand()
            if r < b_n * dt:
                n = n + 1
                freq_b.append(t)
            t += dt

    for i in trange(n_runs):
        n = pop
        t = dt
        while n == pop:
            r = np.random.rand()
            if r < d_n * dt:
                n = n + 1
                freq_d.append(t)
            t += dt
    np.save("freq_b",freq_b)
    np.save("freq_d",freq_d)
    print('mean(b_n) = ' + str(sum(freq_b) / len(freq_b)))
    print('mean(d_n) = ' + str(sum(freq_d) / len(freq_d)))
    '''
    plt.figure()
    plt.hist(freq_d, bins=int(1 / dt), density=True, label='P(t_d)')
    t_max = max(freq_d)
    x = np.linspace(0, t_max, n_runs)
    y = np.exp(-d_n * x)
    plt.plot(x, y, label='-d_n*t')
    plt.yscale('log')
    plt.legend()
    
    plt.figure()
    plt.hist(freq_b, bins=int(1 / dt), density=True, label='P(t_b)')
    t_max = max(freq_b)
    x = np.linspace(0, t_max, n_runs)
    y = np.exp(-b_n * x)
    plt.plot(x, y, label='-b_n*t')
    plt.yscale('log')
    plt.legend()
    plt.show()
'''
    freq_b = np.load("freq_b.npy")
    #print(freq_b)
    freq_d = np.load("freq_d.npy")
    #print(freq_d)
    Tmax = 10
    t = [dt*i for i in range(int(Tmax/dt)+1)]
   # print(t)
    R = 2
    n = np.ones([R, int(Tmax/dt)+1])
    #print(np.shape(n))

    for real in range(R):
        tin = 0
        print(real)
        index_old = 0
        while tin < Tmax-1:
            tb = freq_b[np.random.randint(0,len(freq_b))]
            td = freq_d[np.random.randint(0,len(freq_d))]
            tbar = min(tb, td)
            tin = tin+tbar
            index = np.floor((tin-0)/tbar)+1
            index = int(index)
            n[real, index_old:index-1] = n[real, index_old]
            n[real, index] = n[real, index_old] + 1
            index_old = index
    print(n)
    for i in range(R):
        plt.plot(n[i, :])
    plt.figure()
    print(np.log(n[1,:]))
    plt.plot(-np.log(n[1,:]))
    #print(n)
    plt.show()