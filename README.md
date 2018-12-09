
# Polar Plots
### Plot nice and quick polar maps with one line of code
Plot maps in polar stereographic projections with Matplotlib (Basemap and Numpy). With only one line of code, you can make decent-looking plots, that would normally take some 20-30 lines, customizations, and time.

### Example data
Here, we are using the file [pattern.nc](https://github.com/davidmnielsen/polarplots/blob/master/pattern.nc), which contains the first 3 EOF's of Northern Hemisphere SLP. The 1st EOF is the pattern in which the North Atlantic Oscillation is based. A reference for this plot is available at NOAA's website [here](http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/ao.loading.shtml), where good old GrADS was appearently used.

```python
# Usual imports
import numpy as np
import xarray as xr
import pandas as pd

# Import this module manually
import polarplots as pp

# Load example data
ds=xr.open_dataset('pattern.nc', decode_times=False) 
mylat=ds['lat'].values             
mylon=ds['lon'].values
myvar=ds['var151'][0,:,:].values

```
### Example 1: the simplest plot
```python
myfig=pp.polaranom(mylat,mylon,myvar)
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex1.png "ex1.png")

Save your figure in different formats and resolutions:
```python
myfig.savefig('ex1.pdf') 
myfig.savefig('ex1.png', dpi=300) 
```
Note that some automatic assumptions have been made:
- The range (`vmin` and `vmax`) and intervals (`inc`) of the colorbar are set according to the data. Some rounds are made, so that "beautiful" numbers are displayed.
- The data are assumed to be anomailies. Therefore, the interval -inc<0<inc is set to white, and the zero line is not shown. To undo, set `show0=1`.
- The minimum latitude is set according to the given array of latitudes. Change mannualy using `lat0=45`, for example.
- The colorbar is set to `BuYlRd_r`. Check other possibilities in [here](https://matplotlib.org/examples/color/colormaps_reference.html) and use `cbar='Spectral'` to switch, for example. 

### Example 2: useful customizations
Here, we use explicit definitions of minimum, maximum, and increment values, turn contour lines on - a thicker contour line for the zero line - include left and right-hand side titles, a label for the colobar, set a minimum latitude value, and finally change the colormap style. 
```python
myfig=pp.polaranom(mylat,mylon,myvar,
                   vmin=-3.5,vmax=3.5,inc=0.5,
                   contours=1,zeroline=1,lat0=20,
                   rtitle='EOF1 SLP',
                   ltitle='ERA Interim',
                   clabel='loadings'
                   cmap='BuRd_r'
                   )
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex2.png "ex2.png")

### Example 3: Simple panels
To combine several figures in one panel, specify `ncols` and `nrows` for the number of columns and rows. Each figure is placed within the panel according to the counter `mapid`.  In order to place subplots within the same panel, the figure object needs to be passed as an argument from the 2nd plot on, using the argument `figure`:
```python
myfig=pp.polaranom(mylat,mylon,myvar,
                ncols=2,nrows=1,mapid=1)

myfig=pp.polaranom(mylat,mylon,myvar,
                ncols=2,nrows=1,mapid=2
                figure=myfig) # here we provide the figure object generated in the previous plot

myfig.savefig('panel_1x2.pdf')
``` 
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/panel_1x2.png "panel_1x2.png")

### Example 4: bigger panels
```python
nrows=4
ncols=3

for i in range(12):
    if i==0:
        myfig=pp.polaranom(mylat,mylon,myvar,lat0=30,clabel='colorbar label',ltitle='%d' %(i+1),
                        nrows=nrows, ncols=ncols,mapid=i+1)
    else:
        myfig=pp.polaranom(mylat,mylon,myvar,lat0=30,figure=myfig,ltitle='%d' %(i+1),
                        nrows=nrows, ncols=ncols,mapid=i+1)

myfig.savefig('panel_4x3.pdf')
```

### Example 5: less useful customizations
In this example, the argument `show0` is set to 1 to force the colorbar to show the number 0. This can be useful for cases when data are not anomalies, and sequential color scales are used. We also change the colormap and turn on the arguably nice-looking frame, adapted from [this forum post](https://stackoverflow.com/questions/47431242/matplotlib-create-lat-lon-white-black-round-bounding-box-around-basemap).  

```python
myfig=pp.polaranom(mylat,mylon,myvar+5,
                vmin=3.5,vmax=8.5,inc=0.25,
                cmap='viridis',
                show0=1,
                frame=1)
myfig.savefig('spectral.pdf')
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/spectral.png "spectral.png")

David Nielsen

davidnielsen@id.uff.br


