# calc_cartesian_average

```python
py -m  foampyaverager.scripts.calc_cartesian_average --case --time --var --directions
```
Perform domain averaging in a cartesian direction (i.e., x, y, z) for a case with a structured block or curvilinear 
mesh.

## Input Arguments
- **--case**: string  
Relative file path to the OpenFOAM case
- **--time**: int or float  
Time directory that the file of the variable to be averaged is located in
- **--var**: string  
File of the variable to be averaged
- **--directions**: x, y or z  
The direction that averaging should be performed

## Outputs
- A unique coordinates file
- An averaged variable file

## Example 1: Averaging in One Direction
Let's perform spanwise (z) averaging on the UMean result at time 1000 for the channel395 tutorial case which has block 
mesh. This can be achieved by running calc_cartesian_average and specifying time 1000, var "UMean" and the z direction:

```python
py -m  foampyaverager.scripts.calc_cartesian_average --case "examples/channel395" --time 1000 --var "UMean" --directions z
```

In this example, the unique coordinates file and averaged variable file returned are called "unique_Cx_Cy" and 
"averaged_UMean".

## Example 2: Averaging in Two Directions
This script can perform domain averaging for up to two directions - simply include the second direction for the 
--directions argument. Let's perform spanwise (z) and streamwise (x) averaging on the same result and time for the 
channel395 case.

```python
 py -m  foampyaverager.scripts.calc_cartesian_average --case "examples/channel395" --time 1000 --var "UMean" --directions x z
```

This produces files called "unique_Cy" and "averaged_UMean" for the unique coordinates and averaged variable files.

## Example 3: Averaging a Curvilinear Mesh Result
We've seen how this script can perform domain averaging for a structured cartesian mesh. Let's now perform domain 
averaging on a curvilinear mesh such as the periodicHill tutorial case. Running the line below in the terminal would 
perform spanwise (z) averaging on the Reynolds stress result at time 1510:

```python
py -m  foampyaverager.scripts.calc_cartesian_average --case "examples/periodicHill" --time 1510 --var "UPrime2Mean" --directions z
```
This produces a unique coordinates file called "unique_Cx_Cy" and an averaged variable file called 
"averaged_UPrime2Mean".
