def draw_round_frame(m, width_percent=0.05, degree=45):
    # Adapted from:
    # https://stackoverflow.com/questions/47431242/matplotlib-create-lat-lon-white-black-round-bounding-box-around-basemap
    from matplotlib.patches import Wedge
    import matplotlib.pyplot as plt
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
        
def myround(x, prec=1, base=.5):
    return round(base * round(float(x)/base),prec)

def myround50(x, prec=1, base=50):
    return round(base * round(float(x)/base),prec)

def myround100(x, prec=1, base=100):
    return round(base * round(float(x)/base),prec)

def myround01(x, prec=1, base=.1):
    return round(base * round(float(x)/base),prec)
        
def polaranom(lat,lon,var,vmin=0,vmax=0,inc=0,lat0=0,frame=0,rtitle='',ltitle='',clabel='',
              zeroline=0,cmap='RdBu_r',contours=0,hemisphere='N',fontsize=8,show0=0,
              resolution='c',figsize=(8,8),triangle=1):
    # Libraries
    import numpy as np
    from mpl_toolkits.basemap import Basemap, addcyclic
    import matplotlib.pyplot as plt
    from matplotlib import cm
    
    figure=plt.figure(figsize=figsize)
    ax = figure.add_subplot(111)
      
    if vmin==0 or vmax==0 or inc==0:
        print('Warning: vmin, vmax and inc were not given.')
        mymin=np.float(np.min(var))
        mymax=np.float(np.max(var))
        if abs(mymin)>abs(mymax):
            vmin=mymin
            vmax=-mymin
        else:
            vmin=-mymax
            vmax=mymax
        if abs(vmax)>1 and abs(vmax)<10 and myround(vmax)>vmax:
            vmax=myround(vmax)
            vmin=myround(vmin)
            if ((vmax*10)%10)==0:
                inc=vmax/10
            else:
                inc=0.5
        elif abs(vmax)>1 and abs(vmax)<10 and myround(vmax)<vmax:
            vmax=myround(vmax)
            vmin=myround(vmin)
            if ((vmax*10)%10)==0:
                inc=vmax/10
            else:
                inc=0.5
            vmax=vmax+inc
            vmin=vmin-inc
        elif abs(vmax)>10 and abs(vmax)<100 and round(vmax,0)>vmax:
            vmax=round(vmax,0)
            vmin=round(vmin,0)
            inc=vmax/10
        elif abs(vmax)>10 and abs(vmax)<100 and round(vmax,0)<vmax:
            vmax=round(vmax,0)
            vmin=round(vmin,0)
            inc=vmax/10
            vmax=vmax+inc
            vmin=vmin-inc
        elif abs(vmax)>=100 and abs(vmax)<500 and myround50(vmax,0)>vmax:
            vmax=myround50(vmax)
            vmin=myround50(vmin)
            inc=50
        elif abs(vmax)>=100 and abs(vmax)<500 and myround50(vmax,0)<vmax:
            vmax=myround50(vmax)
            vmin=myround50(vmin)
            inc=50
            vmax=vmax+inc
            vmin=vmin-inc
        elif abs(vmax)>=500 and abs(vmax)<1000 and myround50(vmax,0)>vmax:
            vmax=myround50(vmax)
            vmin=myround50(vmin)
            if (vmax%100)==0:
                inc=100
            else:
                vmax=vmax+50
                vmin=vmin-50
                inc=100
        elif abs(vmax)>=500 and abs(vmax)<1000 and myround50(vmax,0)<vmax:
            vmax=myround50(vmax)
            vmin=myround50(vmin)
            if (vmax%100)==0:
                inc=100
            else:
                inc=50
            vmax=vmax+inc
            vmin=vmin-inc
            if (vmax%100)==0:
                inc=100
            else:
                inc=50
        elif abs(vmax)>=1000 and myround100(vmax,0)>vmax:
            vmax=myround1000(vmax)
            vmin=myround1000(vmin)
            inc=vmax/10
        elif abs(vmax)>=1000 and myround100(vmax,0)<vmax:
            vmax=myround1000(vmax)
            vmin=myround1000(vmin)
            inc=vmax/10
            vmax=vmax+inc
            vmin=vmin-inc
        elif abs(vmax)>0 and abs(vmax)<=1 and myround01(vmax,0)>vmax:
            vmax=myround01(vmax)
            vmin=myround01(vmin)
            inc=vmax/10
        elif abs(vmax)>0 and abs(vmax)<=1 and myround01(vmax,0)<vmax:
            vmax=myround01(vmax)
            vmin=myround01(vmin)
            inc=myround01(vmax)/10
            vmax=vmax+inc
            vmin=vmin-inc
        else:
            inc=vmax/10
        var[np.where(var>vmax)]=vmax-vmax*0.01
        var[np.where(var<vmin)]=vmin+vmin*0.01
        print('The range will be approximated based on data: vmin %.2f, vmax %.2f, inc %.2f' %(vmin,vmax,inc))
            
    if show0==1:    
        ncolors=np.shape(np.arange(vmin,vmax,inc))[0]
        levels=np.arange(vmin,vmax+inc,inc)
    elif show0==0:
        ncolors=np.shape(np.arange(vmin,vmax,inc))[0]-1
        neglevs=np.arange(vmin,0,inc)
        poslevs=np.arange(inc,vmax+inc,inc)
        levels=np.concatenate((neglevs,poslevs))
    else:
        print('Invalid option: show0 arg. must be 0 or 1.')
        return figure
        
    var_c, lon_c = addcyclic(var, lon)
    
    if hemisphere=='N' or hemisphere=='n':
        proj='npstere'
    elif hemisphere=='S' or hemisphere=='s':
        proj='spstere'
    else:
        print('Invalid hemisphere: should be "N" or "S".')
        return figure
    m = Basemap(projection=proj,lat_0=90,lon_0=0,boundinglat=lat0,resolution=resolution,round=True)
    x, y = m(*np.meshgrid(lon_c,lat))
    cbar=cm.get_cmap(cmap,ncolors)
    #cbar.set_under(color='black')
    #cbar.set_over(color='black')
    m.contourf(x,y,var_c,levels=levels,cmap=cbar)
    m.drawcoastlines(linewidth=0.3)
    m.drawmeridians(np.arange(0, 359, 45), labels=[1,1,1,1],linewidth=0.30, fontsize=fontsize)
    m.drawparallels(np.arange(-90, 91, 30),linewidth=0.3)
    if len(levels)>22:
        cblevels=np.concatenate((levels[1:int((len(levels)/2)+1):2],levels[int(len(levels)/2):-1:2]))
    else:
        cblevels=levels[1:-1]
    cb=plt.colorbar(shrink=0.7,pad=0.08,ticks=cblevels,label=clabel)
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



