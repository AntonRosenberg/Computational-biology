import numpy as np
import matplotlib.pyplot as plt


def plot_wave(u, num_plots, t_max, dt):
    fig, ax = plt.subplots()
    for t in range(num_plots):
        ax.plot(u[int(t*(t_max/(dt*num_plots)))][:], label=f't={int(t*(t_max/num_plots))}')
    plt.title(f'\u03BE = {psi_0}, u0 = {u0:.2f}, velocity c = {(index2 - index1) / int((t_max / (dt * num_plots)))}')
    plt.legend()



def plot_wave_phase(u, num_plots, t_max, dt):
    fig2, ax2 = plt.subplots(nrows=2)
    ax2[0].plot(u[int(2*(t_max / (dt * num_plots)))][:], label=f't={int(2*(t_max / num_plots))}')


if __name__ == '__main__':
    num_plots = 10
    L = 100
    rho = 0.5
    q = 8
    psi_0 = 20
    dt = 0.01
    t_max = 1000
    u0 = (q-1)/2 + np.sqrt(((q-1)/2)**2-q/rho+q)
    u = [[0 for i in range(L)] for j in range(int(t_max/dt))]
    u[0][:] = [u0/(1+np.exp(i-psi_0)) for i in range(L)] # Exercise a-b
    #u[0][:] = [u0 / np.exp((i - psi_0)**2) for i in range(L)] # Exercise c

    for i in range(int(t_max/dt)-1):
        for j in range(L):
            if j == 0:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + u[i][j+1]-u[i][j])*dt+u[i][j]
            elif j == L-1:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + u[i][j-1]-u[i][j])*dt+u[i][j]
            else:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + u[i][j-1]+u[i][j+1]-2*u[i][j])*dt+u[i][j]

    u_rounded1 = [round(num, 1) for num in u[int((t_max/(dt*num_plots)))][:]]
    u_rounded2 = [round(num, 1) for num in u[2*int((t_max / (dt * num_plots)))][:]]
    index1 = u_rounded1.index(3.8)
    index2 = u_rounded2.index(3.8)
    print(f'velocity c = {(index2-index1)/int((t_max/(dt*num_plots)))}')
    plot_wave(u, num_plots, t_max, dt)
    plot_wave_phase(u, num_plots, t_max, dt)
    plt.show()
