import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    alpha = 0.01
    numGen = 300
    R_list = [1+0.1*_ for _ in range(291)]
    eta = np.zeros([numGen, len(R_list)])
    print(np.shape(eta))
    plt.subplot(1,2,1)
    for j, R in enumerate(R_list):
        eta[0, j] = 900
        for i in range(numGen-1):
            eta[i+1, j] = np.copy(R*eta[i, j]*np.exp(-alpha*eta[i, j]))

    for i in range(100):
        plt.plot(R_list, eta[-100+i, :])

    plt.ylabel('\u03B7')
    plt.xlabel('R')

    plt.subplot(1, 2, 2)
    indexRs = [65]
    for l in indexRs:
        plt.plot(np.linspace(1,numGen,numGen),eta[:,l])
    plt.xlabel('t')
    plt.ylabel('\u03B7')
    plt.show()
