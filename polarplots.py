def draw_round_frame(m, width_percent=0.05, degree=45):
    # Adapted from:
    # https://stackoverflow.com/questions/47431242/matplotlib-create-lat-lon-white-black-round-bounding-box-around-basemap
    from matplotlib.patches import Wedge
    ax = plt.subplot(111)
    centre_x = (ax.get_xlim()[0] + ax.get_xlim()[1]) / 2
    centre_y = (ax.get_ylim()[0] + ax.get_ylim()[1]) / 2
    width = abs(centre_x) * width_percent

    inner_radius = abs(centre_x) - width/2
    outer_radius = inner_radius + width

    angle_breaks = list(range(0, 361, degree))

    for i, (from_angle, to_angle) in enumerate(list(zip(angle_breaks[:-1], angle_breaks[1:]))):
        color='white' if i%2 == 0 else 'black'
        wedge = Wedge((centre_x, centre_y), outer_radius, from_angle, to_angle, width=outer_radius - inner_radius, 
                      facecolor=color,
                      edgecolor='black',
                      clip_on=False,
                      ls='solid',
                      lw=1)
        ax.add_patch(wedge)

def polaranom(lat,lon,var,vmin,vmax,inc,lat0=20,frame=0,rtitle='',ltitle='',clabel='',
                 zeroline=0,cmap='RdBu_r',contours=0,hemisphere='N',fontsize=8):
    # Libraries
    import numpy as np
    from mpl_toolkits.basemap import Basemap, addcyclic
    import matplotlib.pyplot as plt
    from matplotlib import cm
    
    figure=plt.figure(figsize=(8,8))
    ax = figure.add_subplot(111)
    
    var[np.where(var>vmax)]=vmax
    var[np.where(var<vmin)]=vmin
    ncolors=np.shape(np.arange(vmin,vmax,inc))[0]-1
    neglevs=np.arange(vmin,0,inc)
    poslevs=np.arange(inc,vmax+inc,inc)
    levels=np.concatenate((neglevs,poslevs))
    var_c, lon_c = addcyclic(var, lon)
    
    if hemisphere=='N' or hemisphere=='n':
        proj='npstere'
    elif hemisphere=='S' or hemisphere=='s':
        proj='spstere'
    else:
        print('Invalid hemisphere: should be "N" or "S".')
        return figure
    m = Basemap(projection=proj,lat_0=90,lon_0=0,boundinglat=lat0,resolution='c',round=True)
    x, y = m(*np.meshgrid(lon_c,lat))
    cbar=cm.get_cmap(cmap,ncolors)
    m.contourf(x,y,var_c,levels=levels,cmap=cbar)
    m.drawcoastlines(linewidth=0.3)
    m.drawmeridians(np.arange(0, 359, 45), labels=[1,1,1,1],linewidth=0.30, fontsize=fontsize)
    m.drawparallels(np.arange(-90, 91, 30),linewidth=0.3)
    if len(levels)>20:
        cblevels=np.concatenate((levels[1:int((len(levels)/2)+1):2],levels[int(len(levels)/2):-1:2]))
    else:
        cblevels=levels[1:-1]
    cb=plt.colorbar(shrink=0.5,pad=0.08,ticks=cblevels,label=clabel)
    cb.ax.tick_params(labelsize=fontsize)
    if zeroline==1:
        m2=plt.contour(x,y,var_c,levels=[0],colors='k',add_colorbar=False)
        plt.clabel(m2, m2.levels, inline=False, fontsize=10, fmt='%.1f')
    if frame==1:
        draw_round_frame(m)
    if contours==1:
        plt.contour(x,y,var_c,levels=levels,colors='k',linewidths=0.5)
    plt.title(rtitle,loc='left')
    plt.title(ltitle,loc='right')
    plt.show()
    return figure

def polaranom0(lat,lon,var,vmin,vmax,inc,lat0=20,frame=0,rtitle='',ltitle='',clabel='',
                 zeroline=0,cmap='RdBu_r',contours=0,hemisphere='N',fontsize=8):
    # Libraries
    import numpy as np
    from mpl_toolkits.basemap import Basemap, addcyclic
    import matplotlib.pyplot as plt
    from matplotlib import cm
    
    figure=plt.figure(figsize=(8,8))
    ax = figure.add_subplot(111)
    
    var[np.where(var>vmax)]=vmax
    var[np.where(var<vmin)]=vmin
    ncolors=np.shape(np.arange(vmin,vmax,inc))[0]
    levels=np.arange(vmin,vmax+inc,inc)
    var_c, lon_c = addcyclic(var, lon)
    
    if hemisphere=='N' or hemisphere=='n':
        proj='npstere'
    elif hemisphere=='S' or hemisphere=='s':
        proj='spstere'
    else:
        print('Invalid hemisphere: should be "N" or "S".')
        return figure
    m = Basemap(projection=proj,lat_0=90,lon_0=0,boundinglat=lat0,resolution='c',round=True)
    x, y = m(*np.meshgrid(lon_c,lat))
    cbar=cm.get_cmap(cmap,ncolors)
    m.contourf(x,y,var_c,levels=levels,cmap=cbar)
    m.drawcoastlines(linewidth=0.3)
    m.drawmeridians(np.arange(0, 359, 45), labels=[1,1,1,1],linewidth=0.30, fontsize=fontsize)
    m.drawparallels(np.arange(-90, 91, 30),linewidth=0.3)
    if len(levels)>20:
        cblevels=np.concatenate((levels[1:int((len(levels)/2)+1):2],levels[int(len(levels)/2):-1:2]))
    else:
        cblevels=levels[1:-1]
    cb=plt.colorbar(shrink=0.5,pad=0.08,ticks=cblevels,label=clabel)
    cb.ax.tick_params(labelsize=fontsize)
    if zeroline==1:
        m2=plt.contour(x,y,var_c,levels=[0],colors='k',add_colorbar=False)
        plt.clabel(m2, m2.levels, inline=False, fontsize=10, fmt='%.1f')
    if frame==1:
        draw_round_frame(m)
    if contours==1:
        plt.contour(x,y,var_c,levels=levels,colors='k',linewidths=0.5)
    plt.title(rtitle,loc='left')
    plt.title(ltitle,loc='right')
    plt.show()
    return figure