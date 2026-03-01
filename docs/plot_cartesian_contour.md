# plot_cartesian_contour

```python
 py -m  foampyaverager.scripts.plot_cartesian_contour --unique_coords_path --avg_var_path --avg_var_col --x_ticks --y_ticks --c_levels --cmap --save_name
```

Create a contour plot for a domain-averaged result after running the calc_cartesian_average script on a cartesian mesh.
This script runs the contourf function from Matplotlib under the hood.

## Input Arguments
- **--unique_coords_path**: string  
Relative file path to the unique coordinates file
- **--avg_var_path**: string  
Relative file path to the averaged variable file
- **--avg_var_col**: int  
Column of the averaged variable to be plotted
- **--x_ticks**: string  
x ticks of the contour plot
- **--y_ticks**: string  
y ticks of the contour plot
- **--c_levels**: string  
contour levels of the contour plot
- **--cmap**: string  
colour map of the contour plot
- **--save_name**: string  
File name for saving the contour plot

## Outputs
- .png file of the contour plot

## Example
Let's plot a contour of the spanwise (z) averaged streamwise velocity (Ux) calculated after running 
calc_cartesian_average on the channel395 case. The unique coordinates file and averaged variable file are called 
"unique_Cx_Cy" and "averaged_UMean" as shown in the first [calc_cartesian_average](calc_cartesian_average.md) 
example. As Ux is the first column in the averaged_UMean file, the avg_var_col index is 0.

```python
 py -m  foampyaverager.scripts.plot_cartesian_contour --unique_coords_path "unique_Cx_Cy" --avg_var_path "averaged_UMean" --avg_var_col 0 --x_ticks "[0, 1, 2, 3, 4]" --y_ticks "[0, 0.5, 1, 1.5, 2]" --c_levels "[0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16]" --cmap "plasma" --save_name "channel395_contour.png"
```
Running this line saves the following figure called "channel395_contour.png":

<p align="center">
<img src="images/channel395_contour.PNG" width="400">
</p>

