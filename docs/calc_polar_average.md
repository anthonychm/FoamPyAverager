# calc_polar_average

```python
py -m  foampyaverager.scripts.calc_polar_average --case --time --var --origin --axial_dir --num_unique_radii
```
Perform domain averaging in the axial (z) and tangential (θ) directions for a case with a structured polar or 
cylindrical mesh.

## Input Arguments
- **--case**: string  
Relative path to the OpenFOAM case
- **--time**: int or float  
Time directory that the file of the variable to be averaged is located in
- **--var**: string  
File of the variable to be averaged
- **--origin**: string  
The origin of the polar or cylindrical mesh, accepted in the format "[y, z]"
- **--axial_dir**: string  
The axial direction of the mesh
- **--num_unique_radii**: int  
The number of expected unique radii cell centres 

## Outputs
- A unique radii file
- An averaged variable file

## Example
Let's perform averaging in the axial and tangential directions on the U result at time 227 for the pipeCyclic tutorial 
case. This case has its origin at y = 0 and z = 0, and its axial direction is x. As there are five mesh layers from the 
origin to the outer pipe surface, the expected number of unique radii is 5. We can use this information to run 
calc_polar_average:

```python
py -m  foampyaverager.scripts.calc_polar_average --case "examples/pipeCyclic" --time 227 --var "U" --origin "[0, 0]" --axial_dir "x" --num_unique_radii 5
```

In this example, the unique radii file and averaged variable file returned are called "unique_radii" and "averaged_U".