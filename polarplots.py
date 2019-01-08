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

def getRange(var,vmin,vmax,inc):
    import numpy as np
    mymin=np.float(np.nanmin(var))
    mymax=np.float(np.nanmax(var))
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
        vmax=myround100(vmax)
        vmin=myround100(vmin)
        inc=vmax/10
    elif abs(vmax)>=1000 and myround100(vmax,0)<vmax:
        vmax=myround100(vmax)
        vmin=myround100(vmin)
        inc=vmax/10
        vmax=vmax+inc
        vmin=vmin-inc
    elif abs(vmax)>=0.1 and abs(vmax)<=1 and myround01(vmax,0)>vmax:
        vmax=myround01(vmax)
        vmin=myround01(vmin)
        inc=vmax/10
    elif abs(vmax)>=0.1 and abs(vmax)<=1 and myround01(vmax,0)<vmax:
        vmax=myround01(vmax)
        vmin=myround01(vmin)
        inc=myround01(vmax)/10
        vmax=vmax+inc
        vmin=vmin-inc
    elif inc==0:
        inc=vmax/10

    print('vmin %.2f, vmax %.2f, inc %.2f' %(vmin,vmax,inc))
    return vmin, vmax, inc

def getCbar(levels,show0,cmap,ncolors):
        import numpy as np
        from matplotlib import cm
        if show0==0:
            from matplotlib.colors import ListedColormap
            viridis = cm.get_cmap(cmap, 256)
            newcolors = viridis(np.linspace(0, 1, 256))
            white = np.array([1, 1, 1, 1])
            newcolors[int(256/2)-1:int(256/2)+1, :] = white
            newcmp = ListedColormap(newcolors)
            cbar=cm.get_cmap(newcmp,ncolors)
        else:
            cbar=cm.get_cmap(cmap,ncolors)

        if len(levels)>22 and len(levels)<49 and show0==0:
            cblevels=np.concatenate((levels[1:int((len(levels)/2)+1):2],levels[int(len(levels)/2):-1:2]))
        elif len(levels)<=22 and show0==0:
            cblevels=levels[1:-1]
        elif len(levels)<=22 and show0==1:
            cblevels=levels[1:-1]
        else:
            cblevels=levels[1:-1:2]
        return cbar, cblevels

def drawbox(boxlat,boxlon,m,boxcol,boxlw,boxls):
    from mpl_toolkits.basemap import Basemap, addcyclic
    import matplotlib.pyplot as plt
    import numpy as np
    for l in range(len(boxlat)-1):
        linlat = np.linspace(boxlat[l],boxlat[l+1])
        linlon = np.linspace(boxlon[l],boxlon[l+1])
        xs,ys = m(linlon,linlat)
        m.plot(xs,ys, lw=boxlw, ls=boxls, color=boxcol)
    return

def polaranom(lat=False,lon=False,var=False,vmin=0,vmax=0,inc=0,lat0=False,frame=0,rtitle='',ltitle='',clabel='',colorbar=1,
              zeroline=0,cmap='RdYlBu_r',contours=0,hemisphere='N',cbfontsize=8,show0=0,shrink=0.8,
              resolution='c',figsize=(8,8),commonbar=None,
              nrows=1,ncols=1,mapid=1,draw=True,
              drawMeridians=True, drawParallels=True,meridFontsize=6,
              boxlat=False, boxlon=False, boxcol='k', boxlw=2, boxls='-',
              boxlat2=False, boxlon2=False, boxcol2='k', boxlw2=2, boxls2='-',
              boxlat3=False, boxlon3=False, boxcol3='k', boxlw3=2, boxls3='-',
              boxlat4=False, boxlon4=False, boxcol4='k', boxlw4=2, boxls4='-',
              boxlat5=False, boxlon5=False, boxcol5='k', boxlw5=2, boxls5='-',
              figure=False, autoformat=True,
              ts=False,tsx=False,tsy=False):
    
    if ts==False:
        # Format set-ups:
        if autoformat:
            if (nrows==4 and ncols==3):
                figsize=(9,12)
                meridFontsize=5
                cbfontsize=8
                colorbar=0
                if mapid==1:
                    commonbar='h'
                    bottom=0.1
                    cbarcoords=[0.15, 0.05, 0.7, 0.02]
            elif (nrows==2 and ncols==2):
                figsize=(10,10)
                meridFontsize=7
                cbfontsize=8
                colorbar=0
                if mapid==1:
                    commonbar='h'
                    bottom=0.1
                    cbarcoords=[0.15, 0.055, 0.7, 0.02]
            elif (nrows==1 and ncols==3):
                figsize=(12,5)
                meridFontsize=7
                cbfontsize=8
                colorbar=0
                if mapid==1:
                    commonbar='h'
                    bottom=0.15
                    cbarcoords=[0.15, 0.1, 0.7, 0.04]
            elif (nrows==1 and ncols==2):
                figsize=(10,6)
                meridFontsize=7
                cbfontsize=8
                colorbar=0
                if mapid==1:
                    commonbar='h'
                    bottom=0.15
                    cbarcoords=[0.15, 0.1, 0.7, 0.04]
            elif (nrows==3 and ncols==1):
                figsize=(5,12)
                meridFontsize=7
                cbfontsize=8
                colorbar=0
                if mapid==1:
                    commonbar='h'
                    bottom=0.1
                    cbarcoords=[0.15, 0.05, 0.7, 0.02]
            else:
                if ((nrows!=1 or ncols!=1) and mapid==1):
                    if commonbar=='h':
                        cbarcoords=[0.15, 0.05, 0.7, 0.02]
                        bottom=0.1
                    elif commonbar=='v':
                        cbarcoords=[0.85, 0.15, 0.02, 0.7]

        import numpy as np
        from mpl_toolkits.basemap import Basemap, addcyclic
        import matplotlib.pyplot as plt

        if mapid==1:
            figure=plt.figure(figsize=figsize)
        ax = plt.subplot(nrows,ncols,mapid)

        if vmin==0 or vmax==0 or inc==0:
            vmin, vmax, inc =getRange(var,vmin,vmax,inc)

        var2=np.where(var>vmax,vmax-inc,var)
        var3=np.where(var2<vmin,vmin+inc,var2)

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

        if lat0==False:
            lat0=min(lat)
        var_c, lon_c = addcyclic(var3, lon)
        var_c=var_c[np.where(lat>=lat0)[0],:]
        lat=lat[np.where(lat>=lat0)[0]]

        if hemisphere=='N' or hemisphere=='n':
            proj='npstere'
        elif hemisphere=='S' or hemisphere=='s':
            proj='spstere'
        else:
            print('Invalid hemisphere: should be "N" or "S".')
            return figure

        m = Basemap(projection=proj,lat_0=90,lon_0=0,boundinglat=lat0,resolution=resolution,round=True)
        x, y = m(*np.meshgrid(lon_c,lat))

        cbar, cblevels = getCbar(levels,show0,cmap,ncolors)

        img=m.contourf(x,y,var_c,levels=levels,cmap=cbar)
        m.drawcoastlines(linewidth=0.3)
        if drawMeridians==True:
            m.drawmeridians(np.arange(0, 359, 45), labels=[1,1,0,0],linewidth=0.30, fontsize=meridFontsize)
        if drawParallels==True:
            m.drawparallels(np.arange(-90, 91, 45),linewidth=0.3)

        if boxlat!=False:
            drawbox(boxlat,boxlon,m,boxcol,boxlw,boxls)
        if boxlat2!=False:
            drawbox(boxlat2,boxlon2,m,boxcol2,boxlw2,boxls2)
        if boxlat3!=False:
            drawbox(boxlat3,boxlon3,m,boxcol3,boxlw3,boxls3)
        if boxlat4!=False:
            drawbox(boxlat4,boxlon4,m,boxcol4,boxlw4,boxls4)
        if boxlat5!=False:
            drawbox(boxlat5,boxlon5,m,boxcol5,boxlw5,boxls5)

        if colorbar==1:
            cb=plt.colorbar(shrink=shrink,pad=0.1,ticks=cblevels,label=clabel,drawedges=False)
            cb.ax.tick_params(labelsize=cbfontsize)
        if zeroline==1:
            m2=plt.contour(x,y,var_c,levels=[0],colors='k')
            plt.clabel(m2, m2.levels, inline=False, fontsize=cbfontsize, fmt='%.1f')
        if frame==1:
            draw_round_frame(m)
        if contours==1:
            plt.contour(x,y,var_c,levels=levels,colors='k',linewidths=0.5)
        plt.title(rtitle,loc='right')
        plt.title(ltitle,loc='left')

        if commonbar=='v':
            figure.subplots_adjust(right=0.8,left=0.05,top=0.95,bottom=0.05)
            cbar_ax = figure.add_axes(cbarcoords)
            mycb=figure.colorbar(img,ticks=cblevels,label=clabel,cax=cbar_ax,drawedges=False)
            mycb.ax.tick_params(labelsize=cbfontsize)
        elif commonbar=='h':
            figure.subplots_adjust(bottom=bottom,top=0.95,left=0.05,right=0.95,hspace=0.1)
            cbar_ax = figure.add_axes(cbarcoords)
            mycb=figure.colorbar(img,ticks=cblevels,label=clabel,cax=cbar_ax, orientation='horizontal',drawedges=False)
            mycb.ax.tick_params(labelsize=cbfontsize)
        if draw:
            plt.show()
    
    else:
        import numpy as np
        import matplotlib.pyplot as plt
        ax = figure.add_subplot(nrows,ncols,mapid)
        if tsx==False:
            ax.plot(tsy)
        else:
            ax.plot(tsx,tsy)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')        
        if draw:
            plt.show()
        
    return figure


