import numpy as np
import matplotlib.pyplot as plt


def plot_wave(u, num_plots, t_max, dt):
    fig, ax = plt.subplots(figsize=(10, 10))
    for t in range(num_plots):
        ax.plot(u[int(t*(t_max/(dt*num_plots)))][:], label=f't={int(t*(t_max/num_plots))}')
    plt.title(f'\u03BE = {psi_0}, u0 = {u0:.2f}, velocity c = {(index2 - index1) / int((t_max / (num_plots)))}')
    plt.legend()


def plot_wave_phase(u, v, num_plots, t_max, dt):
    fig2, ax2 = plt.subplots(nrows=2, figsize=(10, 10))
    ax2[0].plot(u[int(2*(t_max / (dt * num_plots)))][:], label=f't={int(2*(t_max/num_plots))}')
    ax2[1].plot(v, u[int(2*(t_max / (dt * num_plots)))][:], label=f't={int(2*(t_max/num_plots))}')
    ax2[0].set_ylabel('u')
    ax2[0].set_xlabel('x')
    ax2[1].set_ylabel('u')
    ax2[1].set_xlabel('v')

    ax2[0].legend()
    ax2[1].legend()
    ax2[0].set_title(f'Wave front')
    ax2[1].set_title(f'Phase space')


if __name__ == '__main__':
    num_plots = 100
    L = 100
    rho = 0.5
    q = 8
    psi_0 = 50
    dt = 0.01
    t_max = 1000
    u0 = (q-1)/2 - np.sqrt(((q-1)/2)**2-q/rho+q)

    u = [[0 for i in range(L)] for j in range(int(t_max/dt))]
    u[0][:] = [u0/(1+np.exp(i-psi_0)) for i in range(L)] # Exercise a-b
    #u[0][:] = [u0 / np.exp((i - psi_0)**2) for i in range(L)] # Exercise c

    for i in range(int(t_max/dt)-1):
        for j in range(L):
            if j == 0:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + (u[i][j+1]-u[i][j]))*dt+u[i][j]
            elif j == L-1:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + (u[i][j-1]-u[i][j]))*dt+u[i][j]
            else:
                u[i+1][j] = (rho*u[i][j]*(1-u[i][j]/q)-u[i][j]/(1+u[i][j]) + (u[i][j-1]+u[i][j+1]-2*u[i][j]))*dt+u[i][j]


    v = [u[int(2*(t_max / (dt * num_plots)))][i+1]-u[int(2*(t_max / (dt * num_plots)))][i] for i in range(L-1)]
    v[0] = 0
    v.append(0)

    u_rounded1 = [round(num, 1) for num in u[int((t_max/(dt*num_plots)))][:]]
    u_rounded2 = [round(num, 1) for num in u[2*int((t_max / (dt * num_plots)))][:]]

    # Index decided manually depending on which values are present in u_rounded1
    index1 = u_rounded1.index(0)
    index2 = u_rounded2.index(0)

    c = (index2 - index1) / int((t_max / num_plots))

    f_prime = -rho*(1-2*u0/q)+1/((1+u0)**2)
    print(f_prime)
    eigen_values = [-c+np.sqrt(c**2-4*f_prime), -c-np.sqrt(c**2-4*f_prime)]

    print(f'velocity c = {c}, Eigen values = {eigen_values}')

    plot_wave(u, num_plots, t_max, dt)
    plot_wave_phase(u, v, num_plots, t_max, dt)
    plt.show()
