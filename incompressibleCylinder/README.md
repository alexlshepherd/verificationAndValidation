# Drag and Vortex Shedding of an Incompressible Cylinder

This case aims to accurately simulate drag around a cylinder in incompressible flow over a range of Reynolds numbers and thier associated shedding frequency. The simulation was transient and turbulence was simulated using (U)RANS and the K-Omega SST model. Though it may have been more appropriate to switch to a laminar simulation at low Re numbers, the thought was that real world designs see laminar and turbulent regimes simultatneously, so a turbulent model needs to capture laminar flow just as accurately.

A block structured mesh was used consisting of 9,200 cells in the 2D case with y+ ranging from XX to XX for Re_D=1e5. The blockage ratio, diameter to channel width, was 5%.

CFD results were evaluated against the coefficient of drag curve fit from White's Viscous Flows []:
EQN
and the Strohaul number fit from Roshko []:
Sr EQN
Fit EQN
Though the Strohaul number curve fits are only applicable up to XXX, the curve has been extended in the graph below.

Figure 1 shows the CFD drag results are accurate up to the drag crisis which is not captured. Quantitatively, the relative error is 6% on average ranging from 1% to 12% for the 2D CFD data. Figure 2 on the other hand shows that 2D CFD Strohaul number data are not accurate. A case can be made for slowest flows that laminar vortex shedding is captured in the 2D simulations. 

NOTE: 3D simulations in progress

### Notes

The cases were built upon the example files provided with OpenFOAM (PATH) and used the block-structured mesh of WOLF. Through testing, I found that it was nesecary for wall adjacent cells to be well outside the turbulent buffer layer the above level of accuracy over the full Re sweep. This would presumably also work if the cells were all inside the viscous layer for all Re numbers. A very fine mesh is required for this since y+ can vary by about 50% over the cylinder, from stagnation to separation. As such, this idea is untested.

### OpenFOAM Specific Notes

For those wishing to make something similar, I wasn't able to simply convert the 2D OpenFOAM tutorial file to a RANS simulation and get the accuracy shown above over the full Re sweep. As well as the mesh requirements listed in the previous section, I found it nesecary to remove all relaxation factors and change the Crank-Nicolson blending factor from 0.9 to 0.5 to reenforce numerical stability. These changes to the numerics resulted in drag coefficient errors being halved. My understanding of relaxation factors is that they shouldn't affect the converged value, only the speed of convergence. Unfortunately, I don't have an explination for this. 

### Refrences
