import xarray as xr 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

filepath = r'D:\Hackathons\Hack on Mount\OZONE_TENDENCY-NEW_DATA-2018-2021-NASA\OZONE_TENDENCY\2021\tavg3_3d_odt_Nv-202109200712output.2055.webform.nc4'

ds = xr.open_dataset(filepath)

#extracting values from variables
time = ds['time'].values
levels = ds['levels'].values
longitude = ds['longitude'].values
latitude = ds['latitude'].values
doxdtana = ds['doxdtana'].values
doxdtdyn = ds['doxdtdyn'].values


mean_doxdtana = np.nanmean(doxdtana)
median_doxdtana = np.nanmedian(doxdtana)
std_doxdtana = np.nanstd(doxdtana)

mean_doxdtdyn = np.nanmean(doxdtdyn)
median_doxdtdyn = np.nanmedian(doxdtdyn)
std_doxdtdyn = np.nanstd(doxdtdyn)


print(f"Mean doxdtana: {mean_doxdtana}")
print(f"Median doxdtana: {median_doxdtana}")
print(f"Standard Deviation doxdtana: {std_doxdtana}")

print(f"Mean doxdtdyn: {mean_doxdtdyn}")
print(f"Median doxdtdyn: {median_doxdtdyn}")
print(f"Standard Deviation doxdtdyn: {std_doxdtdyn}")


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(doxdtana.flatten(), kde=True, color='blue')
plt.title('Histogram of doxdtana')

plt.subplot(1, 2, 2)
sns.histplot(doxdtdyn.flatten(), kde=True, color='green')
plt.title('Histogram of doxdtdyn')

plt.show()