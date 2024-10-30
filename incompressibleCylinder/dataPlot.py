import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

Re = 40
T0 = 300
U = 1
D = 2

t, _, cd, cl, _, _ = np.loadtxt(f"2DdataFiles/2Dcoefficient{Re}.dat", unpack=True)

cd = cd[t>T0]
cl = cl[t>T0]
t = t[t>T0]

dt = t[1] - t[0]
nmax=len(cd)
f, CD = signal.welch(cl, 1/dt, nperseg=nmax)

plt.plot(t, cd)
plt.plot(t, cl)

plt.figure()

plt.plot(f, CD)

i = np.argmax(np.abs(CD))
f_shed = f[i]

Sr = f_shed * D / U

print(f'Reynolds number = {Re:d}')
print(f'Shedding freq. = {f_shed:.3f} Hz')
print(f'Strohaul number = {Sr:.3f}')
print(f'Mean Cd = {np.mean(cd):.3f}')
print(f'Average max/min Cd = {(np.max(cd)+np.min(cd))/2:.3f}')

if Re<=200:
	print(0.212-4.5/Re)
else:
	print(0.212-2.7/Re)

plt.show()
