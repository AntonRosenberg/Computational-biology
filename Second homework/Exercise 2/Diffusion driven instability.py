import numpy as np
from tqdm import trange
import matplotlib.pyplot as plt

def getPeriodicBoundary(state):
    periodicState = np.pad(state,1,"constant")
    periodicState[0,1:-1] = state[-1,:]
    periodicState[-1,1:-1] = state[0,:]
    periodicState[1:-1,-1] = state[:,0]
    periodicState[1:-1, 0] = state[:, -1]
    return periodicState

def getLaplace(state):
    periodicState = getPeriodicBoundary(state)
    lap = np.zeros(np.shape(state))
    for i in range(1,len(periodicState)-1):
        for j in range(1,len(periodicState)-1):
            lap[i-1,j-1] = periodicState[i+1,j]+periodicState[i-1,j]+periodicState[i,j+1]+periodicState[i,j-1]-4*periodicState[i,j]
    #print(lap)
    return lap


state = np.array([[3,4,1],[2,6,4],[2,7,4]])

getLaplace(state)

L = 128
dt = 0.01
Dvlist = [2.3, 3, 5, 9]
#Dv = 2.3
Du = 1
tmax = 10
a = 3
b = 8

u = [np.zeros((L, L)) for i in range(len(Dvlist))]
v = [np.zeros((L, L)) for i in range(len(Dvlist))]
a = 3
b = 8
ustar = a
vstar = b/a

#
#u = np.zeros((L,L))
#v = np.zeros((L,L))
#


for d in range(len(Dvlist)):
    for i in range(L):
        for j in range(L):
            uTemp = u
            u[d][i,j] = ustar - ustar*0.1+np.random.rand(1)*ustar*0.2
            v[d][i,j] = vstar - vstar*0.1+np.random.rand(1)*vstar*0.2



for d in range(len(Dvlist)):
    for i in trange(int(tmax/dt)):
        Dv = Dvlist[d]
        u[d] = u[d] + (a - (b+1)*u[d] + u[d]**2*v[d] + Du*getLaplace(u[d]))*dt
        v[d] = v[d] + (b*u[d]-u[d]**2*v[d] + Dv * getLaplace(v[d])) * dt

        an_array = np.array(u)
        another_array = np.array(uTemp)

        comparison = an_array == another_array
        equal_arrays = comparison.all()
        if equal_arrays:
            print(equal_arrays)
            print(an_array)
            print(another_array)
            print(i)
            break


print(v)
print(np.min(v),np.min(u))
print(np.max(v),np.max(u))
min = np.min([np.min(v),np.min(u)])
max = np.max([np.max(v),np.max(u)])
print(min,max)

print(np.min(u))
print(np.max(u))


for plot in range(len(Dvlist)):
    fig, ax = plt.subplots()
    c = ax.pcolormesh(u[plot], cmap='jet',vmin=min, vmax=max)#
    #c = plt.imshow(u[plot])
    plt.title(f"diffusion: dV = {Dvlist[plot]}")
    fig.colorbar(c, ax=ax)
    #plt.savefig(f"Dv={Dvlist[plot]}".replace(".",",")+".pdf")
'''
fig, ax = plt.subplots()
c = ax.pcolormesh(u[1], cmap='RdBu')
plt.title(f"diffusion: dV = {Dvlist[1]}")
fig.colorbar(c, ax=ax)

fig, ax = plt.subplots()
c = ax.pcolormesh(u[2], cmap='RdBu')
plt.title(f"diffusion: dV = {Dvlist[2]}")
fig.colorbar(c, ax=ax)

fig, ax = plt.subplots()
c = ax.pcolormesh(u[3], cmap='RdBu')
plt.title(f"diffusion: dV = {Dvlist[3]}")
fig.colorbar(c, ax=ax)

'''
#plt.show()
