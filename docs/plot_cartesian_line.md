# plot_cartesian_line

```python
 py -m  foampyaverager.scripts.plot_cartesian_line --unique_coords_path --avg_var_path --avg_var_col --x_ticks --y_ticks --save_name
```

Create a line plot for a domain-averaged result after running the calc_cartesian_average or calc_polar_average script.

## Input Arguments
- **--unique_coords_path**: string  
Relative file path to the unique coordinates file
- **--avg_var_path**: string  
Relative file path to the averaged variable file
- **--avg_var_col**: int  
Column of the averaged variable to be plotted
- **--x_ticks**: string  
 x ticks of the line plot
- **--y_ticks**: string  
y ticks of the line plot
- **--save_name**: string  
File name for saving the line plot

## Outputs
- .png file of the line plot

## Example 1: Plotting Cartesian Averaged Result
Let's create a line plot of the streamwise velocity (Ux) after performing spanwise (z) and streamwise (x) averaging 
on the channel395 case. The unique coordinates file and averaged variable file are called "unique_Cy" and 
"averaged_UMean" as shown in the second [calc_cartesian_average](calc_cartesian_average.md) example. As Ux is the 
first column in the averaged_UMean file, the avg_var_col index is 0.

```python
 py -m  foampyaverager.scripts.plot_cartesian_line --unique_coords_path "unique_Cy" --avg_var_path "averaged_UMean" --avg_var_col 0 --x_ticks "[0, 0.5, 1.0, 1.5, 2.0]" --y_ticks "[0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16]" --save_name "channel395_line.png"
```

Running this line saves the following figure called "channel395_line.png":
<p align="center">
<img src="images/channel395_line.PNG" width="400">
</p>

## Example 2: Plotting Polar Averaged Result
Let's create a line plot of the averaged velocity in the radial (r) direction after performing axial (z) and 
tangential (θ) averaging on the pipeCyclic case. The unique radii file and averaged variable file are called 
"unique_radii" and "averaged_U" as shown in the [calc_polar_average](calc_polar_average.md) example. As velocity 
in the radial direction is the second column in the averaged_U file, the avg_var_col index is 1.

```python
 py -m foampyaverager.scripts.plot_cartesian_line --unique_coords_path "unique_radii" --avg_var_path "averaged_U" --avg_var_col 1 --x_ticks "[0, 0.1, 0.2, 0.3, 0.4, 0.5]" --y_ticks "[0, 0.1, 0.2, 0.3, 0.4, 0.5]" --save_name "pipeCyclic_line.png"
```

Running this line saves the following figure called "pipeCyclic_line.png":
<p align="center">
<img src="images/pipeCyclic_line.PNG" width="400">
</p>
