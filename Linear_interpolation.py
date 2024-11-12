import pandas as pd
import numpy as py

# Load the Excel file
file_path = 'path_to_your_file.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Replace with the name of your sheet, if necessary

# Read the Excel file and load only specific columns
# Here, specify the columns you want to export, e.g., 'Date and Time', 'No of cab bookings', 'Weather condition'
columns_to_export = ['Date and Time', 'No of cab bookings', 'Weather condition']
df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_to_export)

#Assume missing value of 'Weather Condition' at 'Today's Date and 11:00 AM'
df = df.set_index('Date and Time')

#Interpolate to fill missing Weather Condition at 11:00 AM
df['Weather Condition'] = df['Weather Condition'].interpolate(method='linear')
