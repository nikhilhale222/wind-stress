#!/usr/bin/env python
#Importing modules
import numpy as np
import xarray as xr
import os
import matplotlib.pyplot as plt
import matplotlib.axes as ax


os.getcwd()
os.chdir('/Users/nikhilhale/Documents/IITM/LSASI/')
os.getcwd()
f = xr.open_dataset("mon_meanws_2011-20.nc")
d = xr.open_dataset("dragco.nc")
print(d)

#Plotting data variable with upper and lower limit on colorbar
#f.rf[765].plot(vmin=0, vmax=150)
rho=1
#Mean along the axis

d2=d.cdww
lat=f.latitude
lon=f.longitude-180
#dr=xr.DataArray(d.cdww.mean(dim='time'))
#lon=lon-180

u=f.u10
v=f.v10

#wind vector and windstress calculation
vec =  u + 1j * v
spd = np.abs(vec)
ang = np.angle(vec, deg=True)
ang = np.mod(90 - ang, 360)

wind=xr.DataArray(np.sqrt(u**2+v**2))
tau1=rho*(wind**2)*(d.cdww)

#tau=xr.DataArray(np.roll(tau1,-180,axis=2))
lat1, lon1=np.meshgrid(lon, lat)

u=f.u10*(d.cdww)/(d.cdww)
v=f.v10*(d.cdww)/(d.cdww)

tau=xr.DataArray(np.roll(tau1,-360,axis=2))
u10=xr.DataArray(np.roll(u,-360,axis=2))
v10=xr.DataArray(np.roll(v,-360,axis=2))

#%%
i=0
while i<12:
    #contourplot for all months
    b=plt.contourf(lat1[::2,::2],lon1[::2,::2],tau[i,:,:],levels=[0.025,0.05,0.075,0.1,0.125,0.15,0.175],cmap='jet', extend='both')

#This is an alternate but less useful syntex for 
    #tau1.isel(time=i).plot(cmap='jet',levels=[0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2],extend='both', label="windstress")

    #vectorplot over the contourplot
    plt.quiver(lat1[::30,::40], lon1[::30,::40], u10[i,::15,::20], v10[i,::15,::20])#,color='w')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(b,label="Windstress(Pa)")
    plt.title("month=%d"%(i+1))
    plt.savefig("windstress_month{y}.png".format(y=i+1))
    plt.show()
    i+=1
#sum1.plot(vmin=0, vmax=10)

#Grouping by
#ppt.sel(lat=20,lon=80).plot()

#print(f.time.dt.month)

#gb=f.groupby(f.time.dt.month)
#print(gb)


#Time mean

#ds_mm = gb.mean(dim="time")
#print(ds_mm)

#ds_mm.rf.sel(lon=80, lat=20).plot()

#(ds_mm.rf.sel(month=8)-ds_mm.rf.sel(month=6)).plot()

#Zonal Mean
#ds_mm.rf.mean(dim="lat").plot.contourf(x="month", levels=11, vmin=0, vmax=10)

#Climatological mean
#(ds_mm.rf.sel(month=7) - ds_mm.rf.sel(month=6)).plot(vmax=10)



