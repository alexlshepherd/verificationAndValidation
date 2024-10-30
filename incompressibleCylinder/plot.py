import numpy as np
import matplotlib.pyplot as plt

def fit1(ReD):
	# From White's Viscous Flows. Eqn (3-228).
	return 1 + 10 / ReD**0.667
	
def fit2(ReD):
	# From White's Viscous Flows. Eqn. (3-229).
	return (1.18 + 6.8 / (ReD**0.89) + 1.96 / (ReD**0.5) - 
		4e-4 * ReD / (1 + 3.64e-7 * ReD**2))

def roshko(ReD):
	if ReD<200:
		return 0.212 - 4.5 / ReD
	return 0.212 - 2.7 / ReD
vRoshko = np.vectorize(roshko)

Re, cd2D, sr2D = np.loadtxt('2Ddata.dat', unpack=True)

#ReSweep = np.concatenate((np.linspace(1, 200), )

ReSweep = np.logspace(-1, 6, num=100)

plt.loglog(Re, cd2D, '.', label='2D CFD')
plt.loglog(ReSweep, fit2(ReSweep), label='White curve fit')

plt.xlabel(r'$\mathrm{Re}_D$')
plt.ylabel(r'$C_D$')
plt.axis([1, 2e6, 0.1, 10])
plt.title("Coefficient of Drag")
plt.legend()

plt.figure()


plt.plot(Re, sr2D, '.', label='2D CFD')
plt.plot(ReSweep, vRoshko(ReSweep), label='Roshko curve fit')

plt.xlabel(r'$\mathrm{Re}_D$')
plt.ylabel(r'$Sr_D$')
plt.xscale('log')
plt.axis([50, 2e6, 0, 0.3])
plt.legend()
plt.title("Strouhal Number")

relError2D = (cd2D - fit2(Re)) / fit2(Re)

print("Relative Error 2D data:", relError2D)
print(f"Percent RMSE: {np.sqrt(np.mean(relError2D**2))*100:.1f}%")

plt.show()
