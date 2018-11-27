# Polar Plots
## Make a nice and quick plot with one line of code
The objective of this simple module is to make your life easier when ploting maps in polar stereographic projections with Matplotlib (and Numpy). With only one line of code, you can make decent-looking plots, that would normally take some 20-30 lines, customizations, and time.

### Example 1: the simplest plot
Here, we are using the file [pattern.nc](https://github.com/davidmnielsen/polarplots/blob/master/pattern.nc), which contains the first 3 EOF's of Northern Hemisphere SLP. The 1st EOF is the pattern in which the North Atlantic Oscillation is based.
```python
# Usual imports
import numpy as np
import xarray as xr
import pandas as pd

# Import this module manually
import sys
sys.path.append('/your/local/path') 
import polarplots as pp

# Load example date
ds=xr.open_dataset('pattern.nc', decode_times=False) 
mylat=ds['lat'][:]
mylon=ds['lon'][:]
myvar=ds['var151'][0,:,:]

# Simple plot, automatic color range and no customizations:
myfig=pp.polaranom(mylat,mylon,myvar)

# Save figure:
myfig.savefig('/your/local/path/ex1.png', dpi=300)
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex1.png "polaranom ex1.png")

### Example 2: useful customizations
Note that, in example 1, the colorbar is automatically set to data values (symetrically, zero not shown), and the minimum latitude is set to 0°. Now, we use the same data, but the plot is a bit customized with explicit definitions of minimum, maximum, and increment values, turning line contours on, a thicker contour for the zero line, left and right-hand side titles, a label for the colobar, and setting a minimum latitude value.
```python
myfig=pp.polaranom(mylat,mylon,myvar,
                   vmin=-3.5,vmax=3.5,inc=0.5,
                   contours=1,zeroline=1,lat0=20,
                   ltitle='EOF1 SLP',
                   rtitle='ERA Interim',
                   clabel='loadings')
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex2.png "polaranom ex2.png")

### Example 3: less useful customizations
In this example, the argument `show0` is set to 1 to force the colorbar to show the number 0. In the previous examples, the zero was contained in the middle color interval. We also change the colormap and turn on the arguably nice-looking frame, adapted from [this forum post](https://stackoverflow.com/questions/47431242/matplotlib-create-lat-lon-white-black-round-bounding-box-around-basemap).  
```python
myfig=pp.polaranom(mylat,mylon,myvar,vmin=-3.5,vmax=3.5,inc=0.5,lat0=20,
                   cmap='RdYlGn_r',
                   show0=1,
                   frame=1)
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex3.png "polaranom ex3.png")

Feel free to contact me: 

David M. Nielsen

david.buzios@gmail.com


