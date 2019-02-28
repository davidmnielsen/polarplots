
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
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/ex1.png "ex1.png")

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
                   clabel='loadings',
                   cmap='RdBu',
                   )
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/ex2.png "ex2.png")

### Example 3: Simple panels
To combine several figures in one panel, specify `ncols` and `nrows` for the number of columns and rows. Each figure is placed within the panel according to the counter `mapid`.  In order to place subplots within the same panel, the figure object needs to be passed as an argument from the 2nd plot on, using the argument `figure`. For some common set ups, a common colorbar is automatically drawn.

```python
myfig=pp.polaranom(mylat,mylon,myvar,
                ncols=2,nrows=1,mapid=1, draw=False)

myfig=pp.polaranom(mylat,mylon,myvar,
                ncols=2,nrows=1,mapid=2, draw=True, # we just draw the figure on the screen when all subplots are ready
                figure=myfig) # here we provide the figure object generated in the previous plot

myfig.savefig('panel_1x2.pdf')
``` 
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/panel_1x2.png "panel_1x2.png")

### Example 4: bigger panels

Do some smart loops to plot several maps. Don't worry about label location and figure size.

```python
nrows=4
ncols=3

for i in range(12):
    if i==0:
        myfig=pp.polaranom(mylat,mylon,myvar,lat0=30,ltitle='%d' %(i+1),
                        nrows=nrows, ncols=ncols,mapid=i+1, draw=False)
    elif i==11:
        myfig=pp.polaranom(mylat,mylon,myvar,lat0=30,figure=myfig,clabel='colorbar label',ltitle='%d' %(i+1),
                        nrows=nrows, ncols=ncols,mapid=i+1, draw=True)
    else:
        myfig=pp.polaranom(mylat,mylon,myvar,lat0=30,figure=myfig,ltitle='%d' %(i+1),
                        nrows=nrows, ncols=ncols,mapid=i+1, draw=False)

myfig.savefig('panel_4x3.png')
```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/panel_4x3.png "panel_4x3.png")

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
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/spectral.png "spectral.png")

### Example 6: Draw boxes and lines
Use arguments `boxlon` and `boxlat` to provide a list with the coordinates of the corners of a box, as in the example below on the left. Note that the coordinates must be ordered in a cycle. The function simply draws lines between two coordinates, so open polygons or simple lines are also possible. Line color, width and style are controled with arguments `boxcol`, `boxlw` and `boxls`, respectively. Up until 5 elements are possible simultaneously via numbering arguments from the second on:  `boxlon`, `boxlon2`, `boxlo3`... (please feel free to do it in a smarter way).

```python
myfig=pp.polaranom(lat,lon,myvar[0,:,:],ltitle='Simple Box',
                   nrows=1,ncols=2,mapid=1,draw=False,
                   
                   boxlat=[45,80,80,45,45],
                   boxlon=[0,0,150,150,0])

myfig=pp.polaranom(lat,lon,myvar[0,:,:],ltitle='Other usages',
                   nrows=1,ncols=2,mapid=2,draw=True,figure=myfig,
                   
                   boxlat=[45,80,80,45,45],
                   boxlon=[0,0,150,150,0],
                   boxcol='red', boxlw=3,
                   
                   boxlat2=[30,30],
                   boxlon2=[-45,45],
                   boxcol2='green', boxlw2=1,
                   
                   boxlat3=[30,30,50,50,30],
                   boxlon3=[-90,-135,-135,-180,-180],
                   boxcol3='magenta', boxlw3=3.5)

```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/simple_box.png "simple_box.png")

### Example 7: Add hatches (stipplings) and contours
Use the option `returnxy=True` to use the x,y meshgrid generated by Basemap, to add hatches and contours using Matplotlib Pyplot. Note that the option `draw=False` must be used. After adding the ohter graph elements, call `plt.show()`. Valid options for hatch symbols are: `{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}`.

```python
myfig, x, y = pp.polaranom(lat,lon,var,lat0=50,
                          draw=False,returnxy=True,
                          clabel=r'2t [$^{o}$ std(PC1)$^{-1}$]')
          
# add the cyclic longitude
pvalc, lonc = addcyc(pval[lat>50,:],lon) 

# add hatch
z = np.ma.masked_greater(pvalc,0.05)
plt.pcolor(x, y, z, hatch='+', alpha=0.)

# add contour
cont = plt.contour(x, y, pvalc, levels=[0.05,], colors='k')
plt.clabel(cont, inline=True, fontsize=8, fmt='%.2f')

plt.show()

```
![alt text](https://github.com/davidmnielsen/polarplots/blob/master/ex_figures/seasonal_ao_eof_asreg_2t_JJA.png "stipplings and contours")

David Nielsen

davidnielsen@id.uff.br


