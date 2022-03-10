import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
from scipy import stats

def nextTheta(theta,omega,K,nCoupledOscillators,dt):
    for i in range(nCoupledOscillators):
        sum = 0
        for j in range(nCoupledOscillators):
            sum += np.sin(theta[j] - theta[i])
        theta[i] = theta[i] + (omega[i] + K / nCoupledOscillators * sum)*dt
    return theta

if __name__=='__main__':
    gamma = .1

    nCoupledOscillators = 100
    theta = np.random.uniform(-np.pi/2, np.pi/2, size=nCoupledOscillators)


    omega = stats.cauchy.rvs(loc=0,scale=gamma,size=nCoupledOscillators)

    dt = 0.01
    tmax = 10
    K_c=gamma*2
    Klist = K_c*np.array([0.1,1.1,3])
    r = np.zeros(int(tmax/dt))



    for K in Klist:
        for t in trange(int(tmax / dt)):
            sum = np.sum([np.exp(complex(0, theta[k])) for k in range(nCoupledOscillators)])
            if t==0:
                print(np.abs(sum)/nCoupledOscillators)
            theta = nextTheta(theta, omega, K, nCoupledOscillators, dt)
            r[t] = (1 / nCoupledOscillators) * np.absolute(sum)


        plt.plot(r)
        #plt.show()
        plt.ylim([0,1])
        plt.title(f"gamma={gamma},K={K},N={nCoupledOscillators}")
    KlistString = []
    for i in range(len(Klist)):
        KlistString.append("k = " + np.array2string(Klist[i]))

    plt.legend(KlistString)
    plt.title(f"Plot of r(t), $\gamma$={gamma}, $k_c$={K_c}, N={nCoupledOscillators}")
    plt.savefig(f"gamma={gamma},N={nCoupledOscillators}".replace(".",",")+".pdf")
