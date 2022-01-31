import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    alpha = 0.01
    numGen = 300
    R_list = [1+0.1*_ for _ in range(291)]
    eta = np.zeros([numGen, len(R_list)])

    plt.subplot(1, 2, 1)
    for j, R in enumerate(R_list):
        eta[0, j] = 900
        for i in range(numGen-1):
            eta[i+1, j] = np.copy(R*eta[i, j]*np.exp(-alpha*eta[i, j]))

    for i in range(100):
        #plt.plot(R_list, eta[-100+i, :])
        plt.scatter(R_list, eta[-100+i, :], s=0.3)
    plt.ylabel('\u03B7')
    plt.xlabel('R')
    plt.subplot(1, 2, 2)
    Rs = [7.8, 9, 7]
    indexRs = [int((item-1)*10) for item in Rs]
    for l in indexRs:
        plt.plot(np.linspace(1, numGen, numGen), eta[:, l])

    plt.xlim(0, 40)
    plt.xlabel('t')
    plt.ylabel('\u03B7')

    for i in range(len(R_list)):
        if len(np.unique(np.round(eta[:, i]))) > 2:
            Rcrit = R_list[i]
            break
    '''
    for i in range(len(R_list)-1):
            diff = eta[-99, i+1]-eta[-99, i]
            print(diff)
            if diff<0:
                Rcrit = R_list[i]
                break
    '''
    print(Rcrit)

    plt.show()

