import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Replace with the name of your sheet, if necessary

# Read the Excel file and load only specific columns
# Here, specify the columns you want to export, e.g., 'Date and Time', 'No of cab bookings', 'Weather condition'
columns_to_export = ['Date and Time', 'No of cab bookings', 'Weather condition']
df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_to_export)

#Check if any column has missing data
has_missing=df.isna.any().any()
if has_missing;
    print("Data Set has missing data")
else:
    print("Data Set does not have missing data")

#Variable to store missing data count
missing_data_count=df.isna().sum().sum()

