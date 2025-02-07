# Axisymmetric Shock Wave Boundary Layer Interaction (ASWBLI)

This case seeks to recreate the experimental results of Kussoy and Horstman [[1]](https://ntrs.nasa.gov/citations/19890010729) in which a supersonic stream passing over a cylinder interacts with a conical flare. This setup is detailed in the figure below and the results presented here only deal with the 20° flare. Per the experimient, the freestream temperature was 80K and the wall was kept constant at 311K. The initial experimental velocity was Mach 7.05, however its simulated value was 7.11 as advised by NASA's turbulence modeling resources [[2]](https://turbmodels.larc.nasa.gov/axiswblim7_val.html) if the initial ogive isn't modeled, which it wasn't here. The grid used here, also shown below, was a block structured mesh consisting of 20640 hexahedra and the boundary layer cells were placed such y+ was less than 2.

![Experimental Setup](figures/Kussoy_geom.png)
[Grid](figures/grid.png)





### Refrences

[1] M. I. Kussoy and C. C. Horstman, “Documentation of Two- and Three-Dimensional Hypersonic Shock Wave/Turbulent Boundary Layer Interaction Flows,” NASA-TM-101075, Jan. 1989. Accessed: Oct. 19, 2023. [Online]. Available: https://ntrs.nasa.gov/citations/19890010729

[2] Langley Research Center Turbulence Modeling Resources, "ASWBLI: Axisymmetric Shock Wave Boundary Layer Interaction near M=7." [Online]. Available: https://turbmodels.larc.nasa.gov/axiswblim7_val.html




The validation case of Mani et al. [[1]](https://arc.aiaa.org/doi/abs/10.2514/6.1991-3299), with numerical data given by DalBello and Vyas [[2]](https://www.grc.nasa.gov/WWW/wind/valid/channel/study03/channel3.html), is a laminar one-dimensional combustion channel where diatomic hydrogen and oxygen are the reacting fluids. In their numerical simulations, Mani et al. obtained a closed form solution assuming six species and eight reactions, solved using a Runge-Kutta scheme. A mixture of diatomic hydrogen and oxygen flows into the combustion chamber at Mach 1.82 and 1389 K.

The seven species, eight reaction mechanism of Evens and Schexnayder [[3]](https://arc.aiaa.org/doi/10.2514/3.50747), was used for this validation study. Grid convergence is confirmed comparing stream-wise oxygen mass fraction profiles assessed using 400, 600 and 800 cells, coarse, medium and fine sizes respectively. The resulting stream-wise mass fraction profiles obtained using OpenFOAM and the fine mesh to the numerical results of Mani et al., revealing a good level of agreement between the two calculation methods.

![Grid Convergence](figures/gridConvergence.png)

![Mass Fraction](figures/comparision.png)

### Refrences

[1] M. Mani, R. Bush, and P. Vogel, “Implicit equilibrium and finite-rate chemistry models for high speedflow applications,” in 9th Applied Aerodynamics Conference, Baltimore,MD,U.S.A.: American Institute of Aeronautics and Astronautics, Sep. 1991. doi: 10.2514/6.1991-3299.

[2] T. DalBello and M. Vyas, “Channel Combustion.” [Online]. Available: https://www.grc.nasa.gov/www/wind/valid/channel/channel.html

[3] J. S. Evans and C. J. Schexnayder, “Influence of Chemical Kinetics and Unmixedness on Burning in Supersonic Hydrogen Flames,” AIAA Journal, vol. 18, no. 2, pp. 188–193, Feb. 1980, doi: 10.2514/3.50747.

