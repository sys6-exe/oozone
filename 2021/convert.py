import xarray as xr
import pandas as pd
import os

file_path = r'D:\Hackathons\Hack on Mount\OZONE_TENDENCY-NEW_DATA-2018-2021-NASA\OZONE_TENDENCY\2021\tavg3_3d_odt_Nv-202109200712output.2055.webform.nc4'

try:
    # Open the NC4 file using xarray
    ds = xr.open_dataset(file_path)
    print("Dataset opened successfully")
    
    # Print the dataset structure
    print(ds)
    
    # Dictionary to store extracted data
    data_dict = {}

    # Extract and store each variable if it exists
    variables = ['time', 'levels', 'longitude', 'latitude', 'doxdtana', 'doxdtdyn']
    for var in variables:
        if var in ds:
            data_dict[var] = ds[var].values
            print(f"Variable '{var}' extracted successfully, shape: {data_dict[var].shape}")
        else:
            print(f"Variable '{var}' not found in the dataset.")
    
    print("Data extraction complete")
    print(data_dict)

    # Check if data_dict is not empty
    if data_dict:
        # Convert to pandas DataFrame
        df = pd.DataFrame(data_dict)
        print("Data converted to DataFrame")

        # Save DataFrame to CSV in the current working directory
        output_file = 'extracted_data.csv'
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file} in the directory: {os.getcwd()}")
    else:
        print("No data extracted to save to CSV")

except Exception as e:
    print(f"Error opening dataset: {e}")