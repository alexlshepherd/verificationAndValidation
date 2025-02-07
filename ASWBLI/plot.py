import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os

tTot = lambda Ma, T, gamma: T * (1 + (gamma - 1)/2 * Ma**2)

r = 10.15
pInf = 580

models = ["SA", "SST"]

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.5))
fig2, ax3 = plt.subplots(1, 1, figsize=(4, 3.5))
fig3, ax4 = plt.subplots(1, 1, figsize=(4, 3.5))

fig1.suptitle('Surface Normal Profiles 6cm Upstream of Flare')
fig2.suptitle('Wall Pressure Normalized by $p_{w,\infty}(s=-6\mathrm{cm})$')
fig3.suptitle('Wall Heat Flux Normalized by $q_{w,\infty}(s=-6\mathrm{cm})$')

y, U, T0 = np.loadtxt('exp_data/upstream_exp.dat', unpack=True)
ax1.plot(U, y, '.', label='Experiment')
ax2.plot(T0, y, '.')

s, p = np.loadtxt('exp_data/pw_exp.dat', unpack=True)
ax3.plot(s, p, '.', label='Experiment')

s, q = np.loadtxt('exp_data/qw_exp.dat', unpack=True)
ax4.plot(s, q, '.', label='Experiment')

for turbulence in models:
	path = f'postProcessing.{turbulence}/upstreamProbe/0.003/line_Mach_Tt_Ux_gamma.xy'
	
	y, Ma, T, U, gamma = np.loadtxt(path, unpack=True)
	T0 = tTot(Ma, T, gamma)
	
	ax1.plot(U / U[-1], y*100 - r, label=turbulence)
	ax2.plot(T0/T0[-1], y*100 - r)
	
	path = f'postProcessing.{turbulence}/wallValues/0.003/p_wall.raw'
	
	x, y, z, p = np.loadtxt(path, unpack=True)
	s = np.concatenate((x[x<=0], np.sqrt(x**2 + (z - z[0])**2)[x>0]))

	i = np.searchsorted(s, -0.06)
	ax3.plot(s*100, p/p[i], label=turbulence)
	
	path = f'postProcessing.{turbulence}/wallValues/0.003/wallHeatFlux_wall.raw'
	
	x, y, z, q = np.loadtxt(path, unpack=True)
	s = np.concatenate((x[x<=0], np.sqrt(x**2 + (z - z[0])**2)[x>0]))

	i = np.searchsorted(s, -0.06)
	ax4.plot(s*100, q/q[i], label=turbulence)

ax1.set_xlabel('$u/u_\infty$')
ax1.set_ylabel('$y$ [cm]')
ax1.axis([0, 1.2, 0, 3])
ax1.legend()

ax2.set_xlabel('$T_0/T_{0,\infty}$')
ax2.set_ylabel('$y$ [cm]')
ax2.axis([0, 1.2, 0, 3])

ax3.set_xlabel('$s$ [cm]')
ax3.set_ylabel('$p_w/p_{w,\infty}$')
ax3.axis([-10, 15, 0, 14])
ax3.legend()

ax4.set_xlabel('$s$ [cm]')
ax4.set_ylabel('$q_w/q_{w,\infty}$')
ax4.axis([-10, 15, 0, 14])
ax4.legend()

plt.show()
