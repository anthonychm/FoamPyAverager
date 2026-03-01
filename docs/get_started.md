# Get Started

Welcome to the documentation of FoamPyAverager. Here you will find help and examples
for the scripts of this package.

There are two types of scripts in FoamPyAverager: averagers and plotters. 
Averagers perform averaging operations such as spanwise averaging on a specified OpenFOAM case. 
Plotters enable the user to plot and visualise the averaged result. 

Before using an averager, a C file must exist in the time directory to be averaged. 
A time directory is a folder in the OpenFOAM case that contains the results for that time, e.g. 100. 
The C file contains cell centre coordinates and can be obtained by running [writeCellCentres](https://www.openfoam.com/documentation/guides/latest/doc/guide-fos-field-writeCellCentres.html) 
in the OpenFOAM case:

```
postProcess -func writeCellCentres
```
The C file and the file of the results to be averaged must be in ascii format.

## Averagers
[calc_cartesian_average](calc_cartesian_average.md)  
[calc_polar_average](calc_polar_average.md)

## Plotters
[plot_cartesian_contour](plot_cartesian_contour.md)  
[plot_tri_contour](plot_tri_contour.md)  
[plot_cartesian_line](plot_cartesian_line.md)  

## Examples
The following tutorial examples provided with the OpenFOAM software are used to demonstrate how the averagers and 
plotters scripts work.
### 📘 Example 1: Channel395
The [Channel395](https://develop.openfoam.com/Development/OpenFOAM-plus/-/tree/OpenFOAM-v1812/tutorials/incompressible/pimpleFoam/LES/channel395?ref_type=tags) 
case depicts a transient turbulent plane channel flow between two plates. The Reynolds number of the case is 395 based 
on friction velocity, channel half-height and kinematic viscosity. This case can be found in the OpenFOAM folder 
tutorials/incompressible/pimpleFoam/LES.

<p align="center">
<img src="images/channel395_full_domain.PNG" width="400">
</p>

### 📘 Example 2: pipeCyclic
The [pipeCyclic](https://develop.openfoam.com/Development/OpenFOAM-plus/-/tree/OpenFOAM-v1812/tutorials/incompressible/simpleFoam/pipeCyclic?ref_type=tags) 
case depicts a Reynolds-averaged turbulent flow through a circular cross-sectional pipe where only a 
quarter of the domain is modelled. The Reynolds number of the case is 180 based on friction velocity, pipe radius, 
and kinematic viscosity. This case can be found in the OpenFOAM folder tutorials/incompressible/simpleFoam.

<p align="center">
<img src="images/pipeCyclic_full_domain.PNG" width="400">
</p>

### 📘 Example 3: periodicHill
The [periodicHill](https://develop.openfoam.com/Development/OpenFOAM-plus/-/tree/OpenFOAM-v1812/tutorials/incompressible/pimpleFoam/LES/periodicHill?ref_type=tags) 
case demonstrates a transient turbulent flow separating over a hill, creating a recirculation region 
and flow reattachment downstream. The Reynolds number of the case is 12486 based on an inlet velocity of 1.1 m/s, 
hill crest height of 0.03m and kinematic viscosity of $2.643 \times 10^{-6}$ m²/s. This case can be found in 
the OpenFOAM folder tutorials/incompressible/pimpleFoam/LES.

<p align="center">
<img src="images/periodicHill_full_domain.PNG" width="400">
</p>