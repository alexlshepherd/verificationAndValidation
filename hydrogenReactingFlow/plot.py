import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import os
from scipy.optimize import newton

fig, (ax1, ax2) = plt.subplots(1,2)

path = 'postProcessing/centrelineProbe/0.0005/line_H2_H2O_O2.xy'

xO2 , YO2  = np.loadtxt('dataFiles/o2rk.dat' , unpack=True)
xH2 , YH2  = np.loadtxt('dataFiles/h2rk.dat' , unpack=True)
xH2O, YH2O = np.loadtxt('dataFiles/h2ork.dat', unpack=True)

ax1.plot(xH2 , YH2 , 'b.', label='$\mathrm{H_2 \, - \, Numerical}$' )
ax1.plot(xH2O, YH2O, 'gx', label='$\mathrm{H_2O \, - \, Numerical}$')
ax2.plot(xO2 , YO2 , 'r.', label='$\mathrm{O_2 \, - \, Numerical}$' )

x, YH2, YH2O, YO2 = np.loadtxt(os.path.join('Fine', path), unpack=True)

ax1.plot(x*100, YH2 , 'b-' , label='$\mathrm{H_2}$' )
ax1.plot(x*100, YH2O, 'g--', label='$\mathrm{H_2O}$')
ax2.plot(x*100, YO2 , 'r-' , label='$\mathrm{O_2}$' )

ax1.axis([0, 6, 0, 0.055])
ax2.axis([0, 6, 0.9, 1])

ax1.set_ylabel('$Y$')
ax1.set_xlabel('$x\mathrm{\,[cm]}$')
ax2.set_xlabel('$x\mathrm{\,[cm]}$')

ax1.legend()
ax2.legend()

plt.suptitle('Comparing CFD Mass Fractions to Numerical Data')

fig = plt.figure()

for case in ['Coarse', 'Medium', 'Fine']:
	x, YH2, YH2O, YO2 = np.loadtxt(os.path.join(case, path), unpack=True)
	
	plt.plot(x*100, YO2, label='$\mathrm{'+case+'}$')

plt.axis([0, 6, 0.9, 1])

plt.ylabel('$Y_\mathrm{O_2}$')
plt.xlabel('$x\mathrm{\,[cm]}$')

plt.legend()

plt.suptitle('Grid Covergence Demonstrated via Oxygen Mass Fraction ')

plt.show()
