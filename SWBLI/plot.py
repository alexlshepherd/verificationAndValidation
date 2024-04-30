import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

plt.figure(figsize=(5.5,3.5))
pStatic = 4.01e3

cases = ['fine']

x, p = np.loadtxt('experimentalData/wallPressure.dat', unpack=True)
plt.plot(x, p/pStatic, '.', label='Experiment')

for case in cases:
	path = f'{case}/postProcessing/wallProfiles'
	for time in os.listdir(path):
		abspath = os.path.join(path, time, 'pressureProfile_p.xy')
	
		x, p = np.loadtxt(abspath, unpack=True)
		plt.plot(x*1000, p/pStatic, label=case)

plt.xlabel('$x$ [mm]')
plt.ylabel('$p_w/p_I$')

plt.xlim(200, 500)
plt.ylim(0, 10)

plt.suptitle('Wall Pressure Normalized by Inlet Static Pressure ($p_I=4.01$kPa)')

plt.legend()
#plt.show()

matplotlib.rcParams['figure.autolayout'] = False

fig1, (ax1, ax2, ax3, ax4) = plt.subplots(figsize=(10,3.5),nrows=1, ncols=4, sharey=True)

plt.subplots_adjust(wspace=0)


gs2 = plt.figure(figsize=(3,3.5)).add_gridspec(1, 2, hspace=0, wspace=0)
ax5, ax6 = gs2.subplots(sharey='row')

sections = [('section7', ax1), ('section8', ax2), ('section9', ax3),
	('section10', ax4), ('section2', ax5), ('section4', ax6)]

path = 'fine/postProcessing/normalProfiles'

for time in os.listdir(path):
	for section, ax in sections:
		
		y, U, _, _, _ = np.loadtxt(f'experimentalData/{section}.dat', unpack=True)
		ax.plot(U, y, '.')
		
		abspath = os.path.join(path, time, f'{section}_Mach_Tt_Ux_rho.xy')
		y, Ma, T, U, rho = np.loadtxt(abspath, unpack=True)
		ax.plot(U, y*1000, label='OpenFOAM')
		
		ax.set_xlim(300, 900)
		ax.set_ylim(0, 6)
		
		u = U/max(U)
		
		k = np.searchsorted(u, 0.99)
		print(y[k], max(U))
		
		ax.set_title(section.capitalize() + '\ndsf')

#gs.suptitle('ds')

plt.show()



'''
tTot = lambda Ma, T, gamma: T * (1 + (gamma - 1)/2 * Ma**2)

_, (ax1, ax2) = plt.subplots(1, 2, figsize=(6,3.5))

r = 10.15 
y, U, T = np.loadtxt('upstream_exp.dat', unpack=True)

ax1.plot(U, y, '.', label='Experiment')
ax2.plot(T, y, '.')

path = 'postProcessing/upstreamProbe'

for time in os.listdir(path):
	abspath = os.path.join(path, time, 'line_Mach_Tt_Ux_gamma.xy')
	
	y, Ma, T, U, gamma = np.loadtxt(abspath, unpack=True)
	
	T0 = tTot(Ma, T, gamma)
	
	ax1.plot(U / U[-1], y*100 - r, label='OpenFOAM')
	ax2.plot(T0/T0[-1], y*100 - r)


ax1.set_ylabel('$y$ [cm]')
ax1.set_xlabel('$u/u_\infty$')
ax2.set_ylabel('$y$ [cm]')
ax2.set_xlabel('$T_0/T_{0,\infty}$')

ax1.set_xlim(0, 1.2)
ax2.set_xlim(0, 1.2)
ax1.set_ylim(0, 3)
ax2.set_ylim(0, 3)
ax1.legend()

plt.suptitle('Surface Normal Profiles 6cm Upstream of Flare')

pInf = 580

plt.figure(figsize=(4,3.5))

s, p = np.loadtxt('pw_exp.dat', unpack=True)
plt.plot(s, p, '.', label='Experiment')

path = 'postProcessing/wallProbe'
for time in os.listdir(path):
	abspath = os.path.join(path, time, 'line_p.xy')
	s1, p1 = np.loadtxt(abspath, unpack=True)
	
	abspath = os.path.join(path, time, 'line2_p.xy')
	s2, p2 = np.loadtxt(abspath, unpack=True)
	
	s = np.concatenate((s2-0.2, s1))
	p = np.concatenate((p2, p1))
	plt.plot(s*100, p/pInf, label='OpenFOAM')

plt.xlabel('$s$ [cm]')
plt.ylabel('$p_w/p_{w,\infty}$')

plt.xlim(-10, 15)
plt.ylim(0, 14)

plt.suptitle('Wall Pressure Normalized by $p_w(-6\mathrm{cm})=580$Pa')

plt.legend()


plt.show()
'''
